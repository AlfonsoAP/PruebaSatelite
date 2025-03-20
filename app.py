from flask import Flask, render_template;
from flask_socketio import SocketIO;

app = Flask(__name__);
app.config['SECRET_KEY'] = 'jijijija';

socketio = SocketIO(app);

@app.route('/')
def hello_world():
    return 'Adios Mundo';

@socketio.on('connect')
def handle_connect():
    print('Client Connected');

@socketio.on('message')
def handle_message(data):
    print('Received message:', data);
    socketio.emit('response', 'The server received your message: ' + data);

if __name__ == '__main__':
    socketio.run(app, debug=True);
