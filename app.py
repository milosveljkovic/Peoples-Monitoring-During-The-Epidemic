import pymysql
from flask import Flask, request, make_response, jsonify, render_template
from flask_socketio import SocketIO, emit
from random import randrange, randint
from common.calculations import calculate_distance
from flask_cors import CORS
from flaskext.mysql import MySQL
from flask_bootstrap import Bootstrap
import uuid

DB_USER = 'root'
DB_PASS = 'admin1234'
DB_NAME = 'iot'
DB_LOCALHOST = 'localhost'

app = Flask(__name__)
CORS(app)
Bootstrap(app)
app.config['SECRET_KEY'] = 'secret!'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin1234'
app.config['MYSQL_DATABASE_DB'] = 'iot'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql = MySQL()
mysql.init_app(app)
socketio = SocketIO(app, cors_allowed_origins='*')

current_x = 0
current_y = 0
goal_distance = 0
cur_email = ''
path_name = ''


def create_insert_query(user):
    query = f"""INSERT INTO iot.runner(id,name,device,activity_level)
    VALUES("{user['id']}","{user['name']}","{ user['device']}","{user['activity_level']}");
    """
    return query


@app.route('/set_user', methods=['POST'])
def set_user():
    global current_x, current_y, goal_distance, cur_email, path_name
    user = request.json
    insert_query = create_insert_query(user)
    current_x = int(user['x'])
    current_y = int(user['y'])
    goal_distance = int(user['goal_distance'])
    cur_email = user['id']
    path_name = user['path_name']
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
        print("Problem insterting in db :"+str(e))
    finally:
        cursor.close()
        conn.close()


def generate_selectRunners():
    query = """SELECT id FROM iot.runner;"""
    return query


@app.route('/get_user', methods=['GET'])
def get_user():
    select_query = generate_selectRunners()
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(select_query)
        # this will extract row headers
        row_headers = [x[0] for x in cursor.description]
        data = cursor.fetchall()
        json_data = []
        for result in data:
            json_data.append(dict(zip(row_headers, result)))
        return make_response(jsonify(json_data), 200)
    except Exception as e:
        print("Problem insterting in path db :"+str(e))
    finally:
        cursor.close()
        conn.close()


def get_runner_query(runner_id):
    query = f"""SELECT * FROM iot.runner WHERE iot.runner.id="{runner_id}";"""
    return query


@app.route('/runner/<runner_id>', methods=['GET'])
def get_runner(runner_id):
    select_query = get_runner_query(runner_id)
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


def get_runners_path_query(runner_id):
    query = f"""SELECT * FROM iot.path WHERE iot.path.runner_id="{runner_id}" ORDER BY path_x ASC;"""
    return query


def find_averages(data):
    counter = 0
    speed_sum = 0
    heart_rate = 0
    for row in data:
        counter += 1
        speed_sum += row[4]
        heart_rate += row[5]
    return [round(speed_sum/counter,2),round(heart_rate/counter,2)]

@app.route('/path', methods=['GET'])
def get_path():
    runner_id = request.args.get('runner_id', default='*', type=str)
    print(runner_id)
    select_query = get_runners_path_query(runner_id)
    print(select_query)
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
        print(averages)
        for row in data:
            row_data = {'x_path': row[2], 'y_path': row[3], 'distance': row[6]}
            point_array.append(row_data)
        print(point_array)
        json_data = {'points': point_array,'speed_avg':averages[0],'heart_rate_avg':averages[1]}
        return make_response(json_data, 200)
    except Exception as e:
        print("Problem insterting in path db :"+str(e))
        return make_response({'error':'Something went wrong...'}, 400)
    finally:
        cursor.close()
        conn.close()


@socketio.on('connect', namespace='/iot')
def handle_connection():
    print('Connected!')
    emit('connection_success', 200)


@socketio.on('disconnect', namespace='/iot')
def handle_disconnect():
    print('Disconnected!')


def create_query(current_x, current_y,current_distance, speed):
    global cur_email, path_name
    #10,60,1000 put in constants
    query = f"""INSERT INTO iot.path (id, runner_id,path_x,path_y,speed,heart_rate,distance,path_name) VALUES
        ( "{uuid.uuid4()}",(SELECT id from iot.runner WHERE id='{cur_email}'),
        {current_x},{current_y},{speed},{speed*10+60},{round(current_distance/1000, 2)},"{path_name}");
        """
    return query


def save_data(current_x, current_y, distance_per_minut,current_distance):
    speed = distance_per_minut/60  # speed [m/s]
    insert_query = create_query(
        current_x, current_y,current_distance, speed)
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(insert_query)
        conn.commit()
    except Exception as e:
        print("Problem insterting in path db :"+str(e))
    finally:
        cursor.close()
        conn.close()


@socketio.on('start_iot', namespace='/iot')
def start_iot():
    print('Generating data...')
    global current_x, current_y, goal_distance
    current_distance = 0
    distance_per_minut = 0
    timer = 0
    save_data(current_x, current_y,0, 0)
    emit('data_event',
                 {'x': current_x, 'y': current_y, 'new_distance': 0},
                 namespace='/iot')
    while True:
        socketio.sleep(3)
        previous_x = current_x
        previous_y = current_y
        # this should depand of activity_level !?
        current_x = current_x + randrange(30, 200)
        current_y = current_y + randint(-3, 3)
        new_distance = calculate_distance(
            previous_x, previous_y, current_x, current_y)
        current_distance = current_distance+new_distance
        distance_per_minut = distance_per_minut+new_distance
        if(timer >= 60):
            timer = 0
            print(distance_per_minut)
            save_data(current_x, current_y, distance_per_minut,current_distance)
            distance_per_minut = 0
        if(current_distance >= (goal_distance*1000)):
            fill_to_end = (goal_distance*1000)-(current_distance-new_distance)
            emit('data_event',
                 {'x': current_x, 'y': current_y, 'new_distance': fill_to_end},
                 namespace='/iot')
            emit('reach_goal', {
                 'message': 'Good job! You reached your goal!'}, namespace='/iot')
            break
        timer = timer+3
        emit('data_event',
             {'x': current_x, 'y': current_y, 'new_distance': new_distance},
             namespace='/iot')


if __name__ == '__main__':
    socketio.run(app)
