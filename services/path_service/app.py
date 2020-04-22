from flask import Flask, request, make_response, jsonify
from flaskext.mysql import MySQL
from flask_cors import CORS
from db import DB_NAME, DB_USER, DB_PASS, DB_LOCALHOST, generate_get_runners_path_query, create_insert_path_query

# path microservice starts on port 5001
app = Flask(__name__)
CORS(app)

app.config['MYSQL_DATABASE_USER'] = DB_USER
app.config['MYSQL_DATABASE_PASSWORD'] = DB_PASS
app.config['MYSQL_DATABASE_DB'] = DB_NAME
app.config['MYSQL_DATABASE_HOST'] = DB_LOCALHOST

mysql = MySQL()
mysql.init_app(app)


def find_averages(data):
    counter = 0
    speed_sum = 0
    heart_rate = 0
    for row in data:
        counter += 1
        speed_sum += row[4]  # speed
        heart_rate += row[5]  # heart_rate
    return [round(speed_sum/counter, 2), round(heart_rate/counter, 2)]


@app.route('/api/path', methods=['GET'])
def get_path():
    runner_id = request.args.get('runner_id', default='*', type=str)
    select_query = generate_get_runners_path_query(runner_id)
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(select_query)
        data = cursor.fetchall()
        json_data = {}
        point_array = []
        averages = find_averages(data)
        for row in data:
            row_data = {'x_path': row[2], 'y_path': row[3], 'distance': row[6]}
            point_array.append(row_data)
        json_data = {'points': point_array,
                     'speed_avg': averages[0], 'heart_rate_avg': averages[1]}
        return make_response(json_data, 200)
    except Exception as e:
        print("Problem selecting in path db :"+str(e))
        return make_response({'error': 'Something went wrong...'}, 400)
    finally:
        cursor.close()
        conn.close()


@app.route('/api/path/set_path', methods=['POST'])
def set_runner():
    path = request.json
    current_x = path['current_x']
    current_y = path['current_y']
    distance_per_minut = path['distance_per_minut']
    current_distance = path['current_distance']
    cur_email = path['cur_email']
    path_name = path['path_name']
    speed = distance_per_minut/60  # speed [m/s]
    insert_query = create_insert_path_query(
        current_x, current_y, current_distance, speed, cur_email, path_name)
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(insert_query)
        conn.commit()
        reponse_data = {"message": "Successfully added  path!"}
        return make_response(jsonify(reponse_data), 200)
    except Exception as e:
        print("Problem insterting in path db :"+str(e))
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(port=5001, debug=True)
