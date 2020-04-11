from flask import Flask
from flask_socketio import SocketIO, emit
from random import randrange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

x = 10.0
y = 20.0


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


@socketio.on('set_iot_const', namespace='/iot')
def mack_send():
    print('Generating data...')
    while True:
        socketio.sleep(3)
        print('Sending...')
        xx = randrange(10)
        yy = randrange(10)
        x_l = xx
        y_l = yy
        emit('my response', {'x': x_l, 'y': y_l}, namespace='/iot')


if __name__ == '__main__':
    socketio.run(app)
