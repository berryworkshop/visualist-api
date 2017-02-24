schema = {
    'date': {
        'type':'dict',
        'required': True,
        'unique': True,
        'schema': {
            'year': {
                'type': 'number',
                'required': True,
            },
            'month': {
                'type': 'number',
                'required': False,
                'min': 1,
                'max': 12
            },
            'date': {
                'type': 'number',
                'required': False,
                'dependencies': 'month',
                'min': 1,
                'max': 31
            },
            'approximate': {
                'type': 'boolean',
                'default': False
            }
        }
    }
}

span_schema = {
    'start': {
        'type': 'string',
        'data_relation': {
            'resource': 'approx_date',
            'field': '_id',
        }
    },
    'end': {
        'type': 'string',
        'data_relation': {
            'resource': 'approx_date',
            'field': '_id',
        }
    }
}
