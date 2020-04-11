from flask import Flask
from flask_socketio import SocketIO, emit
from random import randrange, randint
from common.calculations import calculate_distance

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

current_x = 50
current_y = 50


@app.route('/', methods=['GET'])
def hello_world():
    return {
        "username": 'message'
    }


@socketio.on('connect', namespace='/iot')
def handle_connection():
    print('Connected!')
    emit('connection_success', 200)


@socketio.on('disconnect', namespace='/iot')
def handle_disconnect():
    print('Disconnected!')


@socketio.on('start_iot', namespace='/iot')
def start_iot():
    print('Generating data...')
    global current_x, current_y
    while True:
        socketio.sleep(3)
        previous_x = current_x
        previous_y = current_y
        current_x = current_x + randrange(2, 10)
        current_y = current_y + randint(-5, 5)
        new_distance = calculate_distance(previous_x, previous_y, current_x, current_y)
        print('Sending x:{} y:{}, new_distance: {}'.format(current_x, current_y, new_distance))
        emit('data_event',
             {'x': current_x, 'y': current_y, 'new_distance': new_distance},
             namespace='/iot')


if __name__ == '__main__':
    socketio.run(app)
