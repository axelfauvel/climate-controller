from flask import request, make_response, abort, jsonify
from flask_restful import Resource
from .manage_ac import power_management, temperature_management
from .manage_data import ManageDatabase


class Power(Resource):
    """
    Class that manages AC power
    """
    def put(self, status):
        """
        Method to manage AC power
        :return:
        """
        if status == 'poweroff':
            if power_management(status):
                return make_response("AC is OFF", 200)
        elif status == 'poweron':
            db = ManageDatabase()
            status = db.get_status()
            if temperature_management(
                    status['ac_mode'],
                    status['temperature'],
                    status['fan']):
                return make_response(
                    "AC is ON \nTemperature : {}°".format(
                        status['temperature']),
                    200)

        abort(400)


class Temperature(Resource):
    """
    Class that manages AC temp
    """
    def put(self):
        """
        change AC temp
        :return:
        """
        if not request.json or not \
                request.json.get('ac_mode') or not \
                request.json.get('temperature') or not \
                request.json.get('fan'):
            abort(400)

        if temperature_management(
                request.json.get('ac_mode'),
                request.json.get('temperature'),
                request.json.get('fan')):
            ManageDatabase().set_status(
                'on',
                request.json.get('ac_mode'),
                request.json.get('temperature'),
                request.json.get('fan'))
            return make_response(
                "AC mode : {}\nTemperature : {}°".format(
                    request.json.get('ac_mode'),
                    request.json.get('temperature')),
                200)

        abort(400)

    def get(self):
        """
        method to retrieve current settings
        :return:
        """
        db = ManageDatabase()
        status = db.get_status()
        return make_response(jsonify(status), 200)

