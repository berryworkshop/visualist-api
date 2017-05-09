import collections
from py2neo import Node

# property types
    # array
    # boolean
    # date
    # date_time
    # decimal
    # dict
    # email
    # image
    # integer
    # integer_positive
    # json
    # path
    # slug
    # string
    # time
    # url
    # uuid

# property arguments
    # blank
    # default
    # help_text
    # max_length
    # min_length
    # options
    # primary_key
    # required
    # schema
    # type
    # unique
    # validators


class BaseModel(Node):

    def __init__(self, *labels, **properties):
        super().__init__(*labels, **properties)
        self.schema = {
            'labels': ['Base'],
            'properties': {
                'slug': {
                    'required': True,
                    'type': 'slug',
                },
                'description': {
                    'type': 'string'
                }
            },
        }

    @classmethod
    def combine_schemas(cls, s1, s2):
        labels = s1.get('labels', [])
        labels.extend(s2.get('labels', []))

        properties = {**s1.get('properties', {}), **s2.get('properties', {})}

        relations = s1.get('relations', [])
        relations.extend(s2.get('relations', []))

        return {
            'labels': labels,
            'properties': properties,
            'relations': relations
        }

    @property
    def date(self):
        pass

    @property
    def url(self):
        pass

    @property
    def json(self):
        pass


class RecordModel(BaseModel):

    def __init__(self, *labels, **properties):
        super().__init__(*labels, **properties)
        schema = {
            'labels': ['Record'],
            'properties': {
                'name': {
                    'required': True,
                    'type': 'string',
                    'default': 'Untitled',
                    'max_length': 200,
                },
                'same_as': {
                    'type': 'url',
                },
                'license': {
                    'required': True,
                    'type': 'url',
                    'default': 'https://creativecommons.org/licenses/by/4.0/'
                },
                'featured': {
                    'type': 'boolean',
                },
                'approved': {
                    'type': 'boolean',
                },
                'web_public': {
                    'type': 'boolean',
                },
                'categories': {
                    'type': 'list',
                },
            },
            'relations': [
                {
                    'direction': 'to',
                    'type': 'HAS_CITATION',
                    'labels': ['Work'],
                },
                {
                    'direction': 'to',
                    'type': 'HAS_SOURCE',
                    'labels': ['Work'],
                },
                {
                    'direction': 'to',
                    'type': 'HAS_TAG',
                    'labels': ['Tag'],
                },
                {
                    'direction': 'to',
                    'type': 'IS_NEXT_ITERATION_OF',
                    'labels': ['Record'],
                },
            ]
        }
        self.schema = super().combine_schemas(self.schema, schema)


    @property
    def citation(self):
        pass

    @property
    def date(self):
        pass
