import datetime as dt
from marshmallow import Schema, fields, post_load


class Event(object):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.category = kwargs.get('category')
        self.description = kwargs.get('description')
        self.uri = kwargs.get('uri')
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<Event(name={self.name!r})>'.format(self=self)


class EventSchema(Schema):
    pk = fields.Integer()
    name = fields.String(required=True)
    category = fields.String(required=True)
    uri = fields.Url()
    description = fields.String()

    @post_load
    def make_event(self, data):
        return Event(**data)
