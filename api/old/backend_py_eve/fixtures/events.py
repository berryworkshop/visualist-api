'owner': {
    'type': 'string',
    'data_relation': {
        'resource': 'users',
        'field': '_id',
    },
},
'name': {'type': 'string'},
'synopsis': {'type': 'string'},
'category': {
    'type': 'list',
    'required': True,
    'allowed': [
        'person',
        'organization',
        'event',
        'work',
        'page',
    ]
},
'slug': {
    'type': 'string',
    'required': True,
    'unique': True,
},
'is_featured': {
    'type': 'boolean',
    'default': False,
},
'tags': {
    'type': 'list',
    'data_relation': {
        'resource': 'tags',
        'field': '_id',
    },
},
'sources': {
    'type': 'dict',
    'schema': {
        'name': {'type': 'string'},
        'remote_id': {'type': 'string'},
        'url': {'type': 'string'},
        'accessed': {'type': 'datetime'},
        'comments': {'type': 'string'},
    }
},
"accounts": {
    'type': 'list',
    'schema': {
        'type': 'dict',
        'schema': {
            'service': {
                'type': 'string',
                'allowed': [
                    'Facebook',
                    'Twitter',
                    'Pinterest',
                ]
            },
            'url': {'type': 'string'},
        }
    }
},
"websites": {
    'type': 'list',
    'schema': {
        'url': {
            'type': 'string',
        }
    }
},
'event_data': {
    'type': 'dict',
    'schema': {
        'category': {
            'type': 'string',
            'required': True,
            'allowed': [
                'exhibition',
                'performance',
                'reception',
            ],
        },
        'description': {'type': 'string'},
        'prices': {
            'type': 'dict',
            'schema': {
                'amount': {'type': 'number'},
                'currency': {
                    'type': 'string',
                    'allowed': list(CURRENCIES.keys())
                },
            }
        }
    }
}
