relation_schema = {
    'note': {
        'type': 'string',
    },
}

reference_schema = {**relation_schema, **{
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
