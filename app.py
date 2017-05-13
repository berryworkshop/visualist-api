from flask import Flask, jsonify
from api.views import EventListView, EventView

app = Flask(__name__)

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
