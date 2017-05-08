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
    # valid
    # validators


class BaseModel(Node):

    schema = {
        'labels': ['Base'],
        'properties': {
            'slug': {
                'required': True,
                'type': 'slug',
            },
            'description': {
                'type': 'text'
            }
        },
        'relations': [
            {
                'direction': 'to',
                'labels': ['Record'],
                'properties': None,
            },
        ]
    }

    def __init__(self, *labels, **properties):
        super().__init(*labels, **properties)

    @property
    def date(self):
        pass

    @property
    def url(self):
        pass

    @property
    def json(self):
        pass
