
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

from instance.config import app_config

db = SQLAlchemy()

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/userregistration/', methods=['POST', 'GET'])
    def userregistration():
        if request.method == "POST":
            username = str(request.data.get('username'))
            if username:
                userregistration = UserRegistration(username=username)
                userregistration.save()
                response = jsonify({
                    'id': userregistration.id,
                    'username': userregistration.username,
                    'date_created': userregistration.date_created,
                    'date_modified': userregistration.date_modified
                })
                response.status_code = 201
                return response

    return app
