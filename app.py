import pickle
from flask import request
from flask import jsonify
import datetime
from flask import Flask, session, g
from flask_socketio import SocketIO
import logging
import warnings

app = Flask(__name__)


@app.route("/ip", methods=["GET"])
def get_my_ip():
    timestamp = datetime.datetime.utcnow()
    with open(f'{request.remote_addr}.last', 'wb') as file:
        file.write(pickle.dumps(timestamp))
    ip = jsonify({'ip': request.remote_addr}), 200
    print('ip', request.remote_addr)
    return ip

if __name__ == '__main__':
    logging.basicConfig(filename='client.log',level=logging.DEBUG)
    app.run(debug=True)                                                                                                                                                                     