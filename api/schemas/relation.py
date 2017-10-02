from .etc import dates_schema


relation_schema = {
    'dates': {
        'type': 'list',
        'schema': dates_schema
    },
    'note': {
        'type': 'string',
    },
}

reference_schema = {**relation_schema, **{
    'pages': {
        'type': 'string',
    },
    'section': {
        'type': 'string',
    },
    'place': {
        'type': 'string',
    },
    'url': {
        'type': 'string',
    },
    'journal': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
            },
            'issue': {
                'type': 'string',
            },
            'volume': {
                'type': 'string',
            },
        }
    },
    'archive': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
            },
            'place': {
                'type': 'string',
            },
            'url': {
                'type': 'string',
            },
            'accessed': {
                'type': 'datetime',
            }
        }
    }
}}
