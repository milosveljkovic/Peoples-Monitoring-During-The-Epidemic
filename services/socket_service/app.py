from flask import Flask
from flask_socketio import SocketIO, emit
from random import randrange, randint
from calculations import calculate_distance
from flask_cors import CORS

M_TO_KM = 1000

# socket microservice starts on port 5002
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')


@socketio.on('connect', namespace='/iot')
def handle_connection():
    print('Connected!')
    emit('connection_success', 200)


@socketio.on('disconnect', namespace='/iot')
def handle_disconnect():
    print('Disconnected!')


@socketio.on('start_iot', namespace='/iot')
def start_iot(data):
    current_x = int(data['current_x'])
    current_y = int(data['current_y'])
    goal_distance = int(data['goal_distance'])
    cur_email = data['cur_email']
    path_name = data['path_name']

    current_distance = 0
    distance_per_minut = 0
    timer = 0
    # save_data(current_x, current_y, 0, 0)
    emit('data_event',
         {
             'x': current_x,
             'y': current_y,
             'new_distance': 0
         },
         namespace='/iot')
    emit('save_data_event',
         {
             'current_x': current_x,
             'current_y': current_y,
             'distance_per_minut': distance_per_minut,
             'current_distance': current_distance,
             'cur_email': cur_email,
             'path_name': path_name
         },
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
            emit('save_data_event', {
                'current_x': current_x,
                'current_y': current_y,
                'distance_per_minut': distance_per_minut,
                'current_distance': current_distance,
                'cur_email': cur_email,
                'path_name': path_name
            },
                namespace='/iot')
            distance_per_minut = 0
        if(current_distance >= (goal_distance*M_TO_KM)):
            emit('save_data_event', {
                'current_x': current_x,
                'current_y': current_y,
                'distance_per_minut': distance_per_minut,
                'current_distance': goal_distance*M_TO_KM,
                'cur_email': cur_email,
                'path_name': path_name
            },
                namespace='/iot')
            fill_to_end = (goal_distance*M_TO_KM) - \
                (current_distance-new_distance)
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
    socketio.run(app, port=5002)
