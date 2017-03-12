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
'work_data': {
    'type': 'dict',
    'schema': {
        'category': {
            'type': 'string',
            'required': True,
            'allowed': [
                'book',
                'artobject',
                'website',
                'installation',
            ]
        },
        'book_data': {
            'type': 'dict',
            'schema': {
                'series': {'type': 'string'},
                'pages': {'type': 'string'},
            }
        },
        'artobject_data': {
            'type': 'dict',
            'schema': {
                'category': {
                    'type': 'string',
                    'required': True,
                    'allowed': [
                        'painting',
                        'drawing',
                        'sculpture',
                        'installation',
                    ]
                },
                "medium": {
                    'type': 'string',
                    'allowed': [
                        'oil on canvas',
                        'acrylic on canvas'
                        'mixed media',
                    ]
                },
            }
        },
        'size': {
            'type': 'dict',
            'schema': {
                'height': {'type': 'number'},
                'width': {'type': 'number'},
                'depth': {'type': 'number'},
                'unit': {
                    'type': 'string',
                    'allowed': [
                        'in',
                        'ft',
                        'mm',
                        'cm',
                        'm',
                    ]
                }
            }
        }
    }
}
