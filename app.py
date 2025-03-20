from flask import Flask, render_template;
from flask_socketio import SocketIO;
from flask_cors import CORS, cross_origin;

app = Flask(__name__);
app.config['SECRET_KEY'] = 'jijijija';
cors = CORS(app);
app.config['CORS_HEADERS'] = 'Content-Type';

socketio = SocketIO(app);

@app.route('/')
@cross_origin()
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
