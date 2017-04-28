from flask import abort, request, jsonify
from flask_restful import Resource, reqparse#, fields, marshal
from py2neo import Graph, Node
from marshmallow import Schema, fields, pprint


from .models import EventSchema
graph = Graph()


def get_highest_event_id():
    highest_id = graph.run('''
        MATCH (e:Event)
        WHERE exists(e.id)
        RETURN e.id
        ORDER BY e.id DESC
        LIMIT 1
        ''').evaluate()

    if highest_id:
        return highest_id
    else:
        return 0

class EventResource(Resource):

    def __init__(self):
        self.schema = EventSchema()

    def get(self, id):
        event = graph.find_one('Event', 'id', id)
        if not event:
            abort(404)
        return dict(event)

    def put(self, id):
        event = graph.find_one('Event', 'id', id)
        if not event:
            abort(404)
        for k, v in args.items():
            if v != None:
                event[k] = v
        graph.push(event)
        return dict(event)

    def delete(self, id):
        event = graph.find_one('Event', 'id', id)
        if not event:
            abort(404)
        graph.delete(event)
        return jsonify({ 'result': True })

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
            abort(400, 'The submitted content does not pass validation.  Please check for spelling errors or missing fields.')

        data, errors = self.schema.dump(event)
        event_node = Node("Event", **data)
        graph.create(event_node)
        return {'event': dict(event_node)}
