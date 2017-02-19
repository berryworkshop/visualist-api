from vocabularies.roles import ROLES

schema = {
    'name': {'type': 'string'},
    'synopsis': {'type': 'string'},
    'acls': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'required': True,
            'schema': {
                'role': {
                    'type': 'list',
                    'allowed': ROLES
                },
                'user': {
                    'type': 'string',
                    'data_relation': {
                        'resource': 'user',
                        'field': '_id',
                    }
                },
                'permissions': {
                    'type': 'dict',
                    'required': True,
                    'schema': {
                        'read': {
                            'type': 'boolean',
                            'default': True
                        },
                        'write': {
                            'type': 'boolean',
                            'default': False
                        }
                    }
                }
            }
        }
    }
}
