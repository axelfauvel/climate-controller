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
        db = ManageDatabase()
        status = db.get_status()

        if status == 'poweroff':
            if power_management(status):
                db.set_status('off',
                              status['ac_mode'],
                              status['temperature'],
                              status['fan'])
                return make_response("AC is OFF", 200)

        elif status == 'poweron':
            if temperature_management(
                    status['ac_mode'],
                    status['temperature'],
                    status['fan']):
                return make_response(
                    "AC is ON \nMode : {}\nTemperature : {}°".format(
                        status['ac_mode'],
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
            abort("Missing mandatory parameter",400)

        settings = {}
        for key in ['ac_mode', 'temperature', 'fan']:
            settings[key] = request.json.get(key)

        if temperature_management(
                settings['ac_mode'],
                settings['temperature'],
                settings['fan']):
            ManageDatabase().set_status(
                'on',
                settings['ac_mode'],
                settings['temperature'],
                settings['fan'])
            return make_response(
                "AC mode : {}\nTemperature : {}°".format(
                    settings['ac_mode'],
                    settings['temperature']),
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

