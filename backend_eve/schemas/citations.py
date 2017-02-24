schema = {
    'category': {
        'type': 'string',
        'required': True,
        'allowed': [
            'webpage',
            'book',
            'journal_article',
            'newspaper_article',
            'artwork',
            'archive_item',
        ]
    },
    'work': {
        'type': 'string',
        'required': True,
        'data_relation': {
            'resource': 'node',
            'field': '_id',
        }
    },
    'abstract': {'type': 'string'},
    'version': {'type': 'string'},
    'via': {
        'type': 'dict',
        'schema': {
            'archive': {
                'type': 'string',
                'required': True,
                'data_relation': {
                    'resource': 'node',
                    'field': '_id',
                },
            'accessed': {
                'type': 'datetime',
                'required': True,
            },
            'url': {'type': 'string'},
            'remote_id': {
                'type': 'string',
                'required': True,
                'data_relation': {
                    'resource': 'identifier',
                    'field': '_id',
                }
            },
        }
    },
    'rights': {
        'data_relation': {
            'resource': 'rights',
            'field': '_id',
        }
    },
    'notes': {'type': 'string'},
    }
}
