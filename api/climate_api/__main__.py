#!/usr/bin/env python3
"""
main module
"""
from flask import flask
from flask_restful import Api
from api_responses import Power, Temperature, CurrentSettings


flask_app = Flask(__name__)
flask_api = Api(flask_app)

flask_api.add_resource(Power, '/v1/power/<status>')
flask_api.add_resource(Temperature, '/v1/temperature')
