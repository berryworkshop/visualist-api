from schemas import base

schema = {
    **base.schema,
    **{
        'synonyms': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'required': True,
                'unique': True,
                'schema': {
                    'term': {'type': 'string'},
                    'vocabulary': {
                        'type': 'string',
                        'allowed': [
                            'Getty Art & Architecture Thesaurus',
                            'Library of Congress Subject Headings',
                        ]
                    },
                    'id': {'type': 'string'},
                    'url': {'type': 'string'},
                }
            }
        }
    }
}
