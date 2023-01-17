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
    ip  = request.remote_addr
    with open(f'last_beat/{request.remote_addr}', 'wb') as file:
        file.write(pickle.dumps(timestamp))
        file.write(pickle.dumps(ip))
    ip = jsonify({'ip': request.remote_addr}), 200
    print('ip:', request.remote_addr)
    return ip

if __name__ == '__main__':
    logging.basicConfig(filename='client.log',level=logging.DEBUG)
<<<<<<< HEAD:watchdog.py
    app.run(debug=True, host='0.0.0.0', port=5000)                                                                                                                                                                     
=======
    app.run(debug=True, host='0.0.0.0', port=5000)                                                                                                                                                                     
>>>>>>> e213d03ede9af6081a115cb0250897e381ae2e12:app.py
