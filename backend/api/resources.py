from flask import abort, request, jsonify
from flask_restful import Resource
from py2neo import Graph, Node
from marshmallow import Schema


from .schemas import EventSchema
graph = Graph()


class EventResource(Resource):
    def __init__(self):
        self.schema = EventSchema()

    def get(self, id):
        event = graph.find_one('Event', 'id', id)
        if not event:
            abort(404)
        return dict(event)

    def put(self, id):
        errors = self.schema.validate(request.json)
        if errors:
            abort(400, {'validation errors': errors })
        event = graph.find_one('Event', 'id', id)
        if not event:
            abort(404)
        for k, v in request.json.items():
            if v != None:
                event[k] = v
        graph.push(event)
        return dict(event)

    def delete(self, id):
        event = graph.find_one('Event', 'id', id)
        if not event:
            abort(404)
        graph.delete(event)
        return 'event {} permanently deleted'.format(id)

class EventListResource(Resource):
    def __init__(self):
        self.schema = EventSchema()

    def get(self):
        events = graph.find('Event')
        if not events:
            abort(404)
        return {'objects': [dict(e) for e in events] }

    def post(self):
        event, errors = self.schema.load(request.json)
        if errors:
            abort(400, {'validation errors': errors })
        event = Node("Event", **request.json)
        graph.create(event)
        return dict(event)

    def delete(self):
        abort(404) # this is a dangerous method for sure
        events = graph.find('Event')
        if not events:
            abort(404)
        for event in events:
            graph.delete(event)
        return 'all events permanently deleted'
