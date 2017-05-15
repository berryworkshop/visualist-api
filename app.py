from flask import Flask, jsonify
import os
from api.views import EventListView, EventView
from settings import DevelopmentConfig, TestingConfig, ProductionConfig
from py2neo import authenticate, Graph


def configure_app(app):
    config = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "default": ProductionConfig,
    }
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])

def init_db():
    '''
    This is for connection; database should already be running externally.
    '''
    # authenticate("localhost:7474", "neo4j", "test_pass")
    db = Graph("http://0.0.0.0:7474/db/data/")


app = Flask(__name__)
configure_app(app)

@app.route('/')
def index():
    return jsonify(
        {
            'links': {
                'events': '/events/'
            }
        }
    )

# app.add_url_rule('/events/', view_func=EventListView.as_view('events'))
# app.add_url_rule('/events/<string:slug>', view_func=EventView.as_view('event'))

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response
