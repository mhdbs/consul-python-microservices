import json
from time import sleep
import socket

import requests
from flask import Flask
app = Flask(__name__)

CONSUL_URL = 'http://consul:8500'

ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 9000

@app.route('/')
def home():
    return 'Hello World from {address}'.format(address=ADDRESS)


@app.route('/health')
def hello_world():
    data = {
        'status': 'healthy'
    }
    return json.dumps(data)

@app.route('/register')
def register():
    url = CONSUL_URL + '/v1/agent/service/register'
    data = {
        'Name': 'microservice_1',
        'Tags': ['flask_app_python'],
        'Address': ADDRESS,
        'Port': 9000,
        'Check': {
            'http': 'http://{address}:{port}/health'.format(address=ADDRESS, port=PORT),
            'interval': '10s'
        }
    }
    app.logger.debug('Reg: ', data)
    res = requests.put(
        url,
        data=json.dumps(data)
    )
    return res.text


if __name__ == '__main__':
    sleep(8)
    try:
        app.logger.debug(register())
    except:
        app.logger.debug('exception happend')
        pass
    app.run(debug=True, host="0.0.0.0", port=PORT)
