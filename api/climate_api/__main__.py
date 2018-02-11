#!/usr/bin/env python3
"""
main module
"""
from flask import Flask
from flask_restful import Api
from .api_responses import Power, Temperature, Timer
from .manage_data import ManageDatabase

flask_app = Flask(__name__)
flask_api = Api(flask_app)

flask_api.add_resource(Power, '/v1/power/<status>')
flask_api.add_resource(Temperature, '/v1/temperature')
flask_api.add_resource(Timer, '/v1/timer')

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8080, ssl_context='adhoc')
    ManageDatabase().init_db()
