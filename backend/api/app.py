from flask import Flask
from flask_restful import Api

from .views import EventListView, EventView


app = Flask(__name__)
app.config['APPLICATION_ROOT'] = "/api/v1/"
app.config['ERROR_404_HELP'] = False

api = Api(app)

app.add_url_rule('/events/', view_func=EventListView.as_view('events'))
app.add_url_rule('/events/<string:slug>', view_func=EventView.as_view('event'))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
