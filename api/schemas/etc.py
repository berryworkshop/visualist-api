source_schema = {
    'format': {
        'type': 'string',
        'allowed': [
            'book',
            'letter',
            'artwork',
            'newspaper article',
            'website',
        ]
    },
    'title': {
        'type': 'string',
    },
    'parent_title': {
        'type': 'string',
    },
    'identifiers': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'system': {
                    'type': 'string',
                    'allowed': [
                        'ISBN',
                        'ISSN',
                        'DOI',
                    ]
                },
                'value': {
                    'type': 'string',
                }
            }
        }
    },
    'authors': {
        'type': 'list',
        'schema': {
            'type': 'string',
        }
    },
    'editors': {
        'type': 'list',
        'schema': {
            'type': 'string',
        }
    },
    'translators': {
        'type': 'list',
        'schema': {
            'type': 'string',
        }
    },
    'archive': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'required': True
            },
            'call_no': {
                'type': 'string',
            },
            'location_in_archive': {
                'type': 'string',
            },
        }
    },
    'publisher': {
        'type': 'string',
    },
    'place': {
        'type': 'string',
    },
    'date': {
        'type': 'string',
    },
    'edition': {
        'type': 'string',
    },
    'volume': {
        'type': 'string',
    },
    'series': {
        'type': 'string',
    },
    'pages': {
        'type': 'string',
    },
    'section': {
        'type': 'string',
    },
    'url': {
        'type': 'string',
    }
}
