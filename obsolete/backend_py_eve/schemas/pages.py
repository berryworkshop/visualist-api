from schemas import base

schema = {
    **base.schema,
    **{
        'category': {
            'type': 'string',
            'required': True,
            'allowed': [
                'standard',
                'article',
            ]
        },
        'slug': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'body': {'type': 'string'}
    }
}
