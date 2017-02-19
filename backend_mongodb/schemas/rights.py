schema = {
    'copyright_owner': {
        'type': 'string',
        'default': 'the author',
    },
    'license': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'allowed': [
                    'all rights reserved',
                    'fair use',
                    'MIT',
                    'BSD',
                    'GPL',
                    'custom'
                ],
            },
            'url': {'type': 'string'}
        }
    }
}
