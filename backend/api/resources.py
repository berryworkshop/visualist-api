from flask import abort, request, jsonify
from flask_restful import Resource, reqparse#, fields, marshal
from py2neo import Graph, Node

from .models import Event
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
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
            type = str,
            location = 'json',
            )
        self.parser.add_argument('description',
            type = str,
            location = 'json',
            )
        super().__init__()
        pass

    def get(self, id):
        event = graph.find_one('Event', 'id', id)
        if not event:
            abort(404)
        return {'event': dict(event)}
        # return { 'event': marshal(event, event_fields) }

    def put(self, id):
        event = graph.find_one('Event', 'id', id)
        if not event:
            abort(404)
        # event = [e for e in events if e['id'] == id][0]
        args = self.parser.parse_args()
        for k, v in args.items():
            if v != None:
                event[k] = v
        graph.push(event)
        return {'event': dict(event)}
        # return { 'event': marshal(event, event_fields) }

    def delete(self, id):
        event = graph.find_one('Event', 'id', id)
        if not event:
            abort(404)
        graph.delete(event)
        return jsonify({ 'result': True })

class EventListResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
            type = str,
            required = True,
            help = 'No event name provided',
            location = 'json',
            )
        self.parser.add_argument('description',
            type = str,
            default = "",
            location = 'json',
            )
        super().__init__()

    def get(self):
        events = graph.find('Event')
        if not events:
            abort(404)
        return {'events': [dict(e) for e in events] }
        # return { 'events': [marshal(event, event_fields) for event in events] }

    def post(self):
        args = self.parser.parse_args()
        properties = {
            'id': get_highest_event_id() + 1,
            'name': request.json['name'],
            'category': request.json.get('category', ""),
            'description': request.json.get('description', ""),
        }
        event = Node("Event", **properties)
        graph.create(event)
        return {'event': dict(event)}
        # return { 'event': marshal(event, event_fields) }
