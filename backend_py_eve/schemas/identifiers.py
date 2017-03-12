schema = {
    'id': {
        'type': 'dict',
        'required': True,
        'unique': True,
        'schema': {
            'category': {
                'type': 'string',
                'allowed': [
                    'slug',
                    'doi',
                    'isbn',
                    'call_number',
                    'ezid',
                ]
            },
            'value': {'type': 'string'}
        }
    }
}
