from flask import Flask
from flask_socketio import SocketIO, send;

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/', methods=['GET'])
def hello_world():
    return {
        "username": 'message'
    }


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
