from flask import Flask, request, jsonify, make_response
from flaskext.mysql import MySQL
from flask_cors import CORS
from db import DB_NAME, DB_USER, DB_PASS, DB_LOCALHOST, create_insert_query, generate_get_runner_query, generate_select_runners_query

# runner microservice starts on port 5000
app = Flask(__name__)
CORS(app)

app.config['MYSQL_DATABASE_USER'] = DB_USER
app.config['MYSQL_DATABASE_PASSWORD'] = DB_PASS
app.config['MYSQL_DATABASE_DB'] = DB_NAME
app.config['MYSQL_DATABASE_HOST'] = DB_LOCALHOST

mysql = MySQL()
mysql.init_app(app)


@app.route('/api/runner/set_runner', methods=['POST'])
def set_runner():
    user = request.json
    insert_query = create_insert_query(user)
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(insert_query)
        conn.commit()
        reponse_data = {"message": "Successfully added user!"}
        return make_response(jsonify(reponse_data), 200)
    except Exception as e:
        print("Problem insterting in iot.runner db :"+str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/api/runner/get_runners', methods=['GET'])
def get_runners():
    select_query = generate_select_runners_query()
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(select_query)
        row_headers = [x[0] for x in cursor.description]
        data = cursor.fetchall()
        json_data = []
        for result in data:
            json_data.append(dict(zip(row_headers, result)))
        return make_response(jsonify(json_data), 200)
    except Exception as e:
        print("Problem with iot.runner db :"+str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/api/runner/<runner_id>', methods=['GET'])
def get_runner(runner_id):
    select_query = generate_get_runner_query(runner_id)
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(select_query)
        data = cursor.fetchone()
        runner = {'id': data[0], 'name': data[1],
                  'device': data[2], 'activity_level': data[3]}
        return make_response(runner, 200)
    except Exception as e:
        print("Problem insterting in path db :"+str(e))
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
