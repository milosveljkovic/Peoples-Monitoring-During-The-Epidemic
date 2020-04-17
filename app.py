import pymysql
from flask import Flask, request, make_response, jsonify, render_template
from flask_socketio import SocketIO, emit
from random import randrange, randint
from common.calculations import calculate_distance
from flask_cors import CORS
from flaskext.mysql import MySQL
from flask_bootstrap import Bootstrap
import uuid

M_TO_KM=1000
FACTOR = 10
BOTTOM_HEART_RATE = 60

DB_USER = 'root'
DB_PASS = 'admin1234'
DB_NAME = 'iot'
DB_LOCALHOST = 'localhost'
SECRET_KET='secret!'

app = Flask(__name__)
CORS(app)
Bootstrap(app)
app.config['SECRET_KEY'] = SECRET_KET
app.config['MYSQL_DATABASE_USER'] = DB_USER
app.config['MYSQL_DATABASE_PASSWORD'] =DB_PASS
app.config['MYSQL_DATABASE_DB'] = DB_NAME
app.config['MYSQL_DATABASE_HOST'] = DB_LOCALHOST

mysql = MySQL()
mysql.init_app(app)
socketio = SocketIO(app, cors_allowed_origins='*')

current_x = 0
current_y = 0
goal_distance = 0
cur_email = ''
path_name = ''

def create_insert_query(user):
    query = f"""
    INSERT INTO iot.runner(id,name,device,activity_level)
    VALUES("{user['id']}","{user['name']}","{ user['device']}","{user['activity_level']}");
    """
    return query

def generate_select_runners_query():
    query = """SELECT id FROM iot.runner;"""
    return query

def generate_get_runner_query(runner_id):
    query = f"""SELECT * FROM iot.runner WHERE iot.runner.id="{runner_id}";"""
    return query

def generate_get_runners_path_query(runner_id):
    query = f"""
    SELECT * FROM iot.path 
    WHERE iot.path.runner_id="{runner_id}" 
    ORDER BY path_x ASC;
    """
    return query

def create_insert_path_query(current_x, current_y,current_distance, speed):
    global cur_email, path_name
    query = f"""
    INSERT INTO iot.path (id, runner_id,path_x,path_y,speed,heart_rate,distance,path_name) 
    VALUES
    ( "{uuid.uuid4()}",(SELECT id from iot.runner WHERE id='{cur_email}'),
    {current_x},{current_y},{speed},{speed*FACTOR+BOTTOM_HEART_RATE},{round(current_distance/M_TO_KM, 2)},"{path_name}");
    """
    return query

@app.route('/api/runner/set_runner', methods=['POST'])
def set_runner():
    global current_x, current_y, goal_distance, cur_email, path_name
    user = request.json
    insert_query = create_insert_query(user)
    cur_email = user['id']
    current_x = int(user['x'])
    current_y = int(user['y'])
    path_name = user['path_name']
    goal_distance = int(user['goal_distance'])
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


@app.route('/api/runner/get_runner', methods=['GET'])
def get_runners():
    select_query = generate_select_runners_query()
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


def find_averages(data):
    counter = 0
    speed_sum = 0
    heart_rate = 0
    for row in data:
        counter += 1
        speed_sum += row[4]     #speed
        heart_rate += row[5]    #heart_rate
    return [round(speed_sum/counter,2),round(heart_rate/counter,2)]

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
        json_data = {'points': point_array,'speed_avg':averages[0],'heart_rate_avg':averages[1]}
        return make_response(json_data, 200)
    except Exception as e:
        print("Problem selecting in path db :"+str(e))
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


def save_data(current_x, current_y, distance_per_minut,current_distance):
    speed = distance_per_minut/60  # speed [m/s]
    insert_query = create_insert_path_query(current_x, current_y,current_distance, speed)
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
        current_x = current_x + randrange(5, 22)
        current_y = current_y + randint(-3, 3)
        new_distance = calculate_distance(
            previous_x, previous_y, current_x, current_y)
        current_distance = current_distance+new_distance
        distance_per_minut = distance_per_minut+new_distance
        if(timer >= 60):
            timer = 0
            save_data(current_x, current_y, distance_per_minut,current_distance)
            distance_per_minut = 0
        if(current_distance >= (goal_distance*M_TO_KM)):
            save_data(current_x, current_y, distance_per_minut,goal_distance*M_TO_KM)
            fill_to_end = (goal_distance*M_TO_KM)-(current_distance-new_distance)
            emit('data_event',
                 {'x': current_x, 'y': current_y, 'new_distance': fill_to_end},
                 namespace='/iot')
            emit('reach_goal', {
                 'message': 'Good job! You reached your goal!'}, 
                 namespace='/iot')
            break
        timer = timer+3
        emit('data_event',
             {'x': current_x, 'y': current_y, 'new_distance': new_distance},
             namespace='/iot')


if __name__ == '__main__':
    socketio.run(app)
