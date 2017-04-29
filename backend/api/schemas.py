import datetime as dt
from marshmallow import Schema, fields, post_load


class Event(object):
    def __init__(self, name, category, description):
        # self.slug = slug
        self.name = name
        self.category = category
        self.description = description
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<Event(name={self.name!r})>'.format(self=self)


class EventSchema(Schema):
    # slug = fields.String(required=True)
    name = fields.String(required=True)
    category = fields.String(required=True)
    # uri = fields.Url()
    description = fields.String()

    @post_load
    def make_event(self, data):
        return Event(**data)
