from schemas import base

schema = {
    **base.schema,
    **{
        'category': {
            'type': 'string',
            'required': True,
            'allowed': [
                'image',
                'video',
                'document',
            ]
        },
        'url': {'type': 'string'},
        'checksum': {'type': 'string'},
        'image_data': {
            'type': 'dict',
            'schema': {
                "format": {
                    'type': 'string',
                    'allowed': [
                        '.tiff'
                        '.gif',
                        '.png',
                        '.jpg',
                        '.pdf',
                    ]
                },
                'aspect': {
                    'type': 'string',
                    'allowed': [
                        'main',
                        'detail',
                        'recto',
                        'verso',
                        'signature',
                    ]
                }
            }
        },
        'document_data': {
            'type': 'dict',
            'schema': {
                "format": {
                    'type': 'string',
                    'allowed': [
                        '.pdf',
                        '.doc',
                    ]
                }
            }
        }
    }
}
