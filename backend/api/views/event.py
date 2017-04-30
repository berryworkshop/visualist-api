from flask.views import MethodView
from flask import jsonify
from ..models import Event

class EventListView(MethodView):
    '''
    /events/
    '''

    def get(self):
        events = [e.__properties__ for e in Event.nodes.all()]
        return jsonify({'objects': events})

    def post(self):
        return 'post event'

class EventView(MethodView):
    '''
    /events/<string:slug>
    '''

    def get(self, slug):
        return 'get {} event'.format(slug)

    def put(self, slug):
        return 'put {} event'.format(slug)

    def delete(self, slug):
        return 'delete {} event'.format(slug)
