import pymysql
from flask import Flask, request, make_response, jsonify,render_template
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
    query="""SELECT id FROM iot.runner;"""
    return query

@app.route('/get_user', methods=['GET'])
def get_user():
    print('usao')
    select_query=generate_selectRunners()
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(select_query)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        data = cursor.fetchall()
        json_data=[]
        for result in data:
            json_data.append(dict(zip(row_headers,result)))
        return make_response(jsonify(json_data), 200)
    except Exception as e:
        print("Problem insterting in path db :"+str(e))
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


def create_query(current_x, current_y, distance_per_minut, speed):
    global cur_email, path_name
    query = f"""INSERT INTO iot.path (id, runner_id,path_x,path_y,speed,heart_rate,distance,path_name) VALUES
        ( "{uuid.uuid4()}",(SELECT id from iot.runner WHERE id='{cur_email}'),
        {current_x},{current_y},{speed},{speed+60},{distance_per_minut},"{path_name}");
        """
    return query


def save_data(current_x, current_y, distance_per_minut):
    speed = distance_per_minut/60  # speed [m/s]
    insert_query = create_query(
        current_x, current_y, distance_per_minut, speed)
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
    while True:
        socketio.sleep(3)
        previous_x = current_x
        previous_y = current_y
        # this should depand of activity_level !?
        current_x = current_x + randrange(20, 100)
        current_y = current_y + randint(-3, 3)
        new_distance = calculate_distance(
            previous_x, previous_y, current_x, current_y)
        current_distance = current_distance+new_distance
        distance_per_minut = distance_per_minut+new_distance
        if(timer >= 60):
            timer = 0
            save_data(current_x, current_y, distance_per_minut)
            distance_per_minut = 0
        if(current_distance >= (goal_distance*1000)):
            fill_to_end=(goal_distance*1000)-(current_distance-new_distance)
            emit('data_event',
             {'x': current_x, 'y': current_y, 'new_distance': fill_to_end},
             namespace='/iot')
            emit('reach_goal', {'message': 'Good job! You reached your goal!'}, namespace='/iot')
            break
        print('Sending x:{} y:{}, new_distance: {}'.format(
            current_x, current_y, new_distance))
        timer = timer+3
        emit('data_event',
             {'x': current_x, 'y': current_y, 'new_distance': new_distance},
             namespace='/iot')


if __name__ == '__main__':
    socketio.run(app)
