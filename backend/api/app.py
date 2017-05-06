from flask import Flask, jsonify
from flask_restful import Api
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware
from neomodel import config

from .views import EventListView, EventView


app = Flask(__name__)
api = Api(app)

prefix = '/v1'
app.wsgi_app = DispatcherMiddleware(run_simple, {prefix: app.wsgi_app})

config.DATABASE_URL = 'bolt://neo4j:neo4j@localhost:7687'  # default


@app.route('/')
def index():
    return jsonify(
        {
            'links': {
                'events': '/events/'
            }
        }
    )

app.add_url_rule('/events/', view_func=EventListView.as_view('events'))
app.add_url_rule('/events/<string:slug>', view_func=EventView.as_view('event'))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
