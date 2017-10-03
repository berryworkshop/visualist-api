from .etc import date_schema, location_schema


relation_schema = {
    # 'dates': {
    #     'type': 'list',
    #     'schema': date_schema
    # },
    # 'locations': {
    #     'type': 'list',
    #     'schema': location_schema
    # },
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
