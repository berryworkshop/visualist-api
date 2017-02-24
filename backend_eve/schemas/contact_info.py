schema = {
    'phones': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'unique': True,
            'required': True,
            'schema': {
                'category': {
                    'type': 'string',
                    'required': False,
                    'allowed': [
                        'office',
                        'mobile',
                    ]
                },
                'country': {
                    'type': 'number',
                    'required': True,
                    'default': 1
                },
                'area': {
                    'type': 'number',
                    'required': True
                },
                'exchange': {
                    'type': 'number',
                    'required': True
                },
                'number': {
                    'type': 'number',
                    'required': True
                },
                'extension': {
                    'type': 'number',
                    'required': False
                },
            }
        }
    },
    'emails': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'unique': True,
            'required': True,
            'schema': {
                'category': {
                    'type': 'list',
                    'allowed': [
                        'personal',
                        'work'
                    ],
                    'default': 'personal'
                },
                'email': {
                    'type': 'string',
                }
            }
        }
    },
    'addresses': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'unique': True,
            'required': True,
            'schema': {
                'category': {
                    'type': 'list',
                    'allowed': [
                        'personal',
                        'work'
                    ],
                    'default': 'personal'
                },
                'address': {
                    'type': 'string',
                    'data_relation': {
                        'resource': 'location',
                        'field': '_id',
                    },
                }
            }
        }
    }
}
