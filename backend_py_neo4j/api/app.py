from flask import Flask
from flask_restful import Api
from .resources import EventResource, EventListResource

app = Flask(__name__)
# app.config['APPLICATION_ROOT'] = "/api/v1.0/"
app.config['ERROR_404_HELP'] = False

api = Api(app)

api.add_resource(EventListResource, '/v1/events',          endpoint = 'events')
api.add_resource(EventResource,     '/v1/events/<int:id>', endpoint = 'event')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
