# property types
    # array
    # boolean
    # date
    # date_time
    # decimal
    # dict
    # email
    # image
    # integer
    # integer_positive
    # json
    # path
    # slug
    # string
    # time
    # url
    # uuid

# property arguments
    # blank
    # default
    # help_text
    # max_length
    # min_length
    # options
    # primary_key
    # required
    # schema
    # type
    # unique
    # validators

def combine(s1, s2):
    return {
        'labels': s1['labels'] + s2['labels'],
        'properties': {**s1['properties'], **s2['properties']},
        'relations': s1['relations'] + s2['relations'],
    }


base_schema = {
    'labels': ['Base'],
    'properties': {
        'slug': {
            'required': True,
            'type': 'slug',
        },
        'description': {
            'type': 'string'
        }
    },
    'relations': [],
}

record_schema = combine(base_schema, {
    'labels': ['Record'],
    'properties': {
        'name': {
            'required': True,
            'type': 'string',
            'default': 'Untitled',
            'max_length': 200,
        },
        'same_as': {
            'type': 'url',
        },
        'license': {
            'required': True,
            'type': 'url',
            'default': 'https://creativecommons.org/licenses/by/4.0/'
        },
        'featured': {
            'type': 'boolean',
        },
        'approved': {
            'type': 'boolean',
        },
        'web_public': {
            'type': 'boolean',
        },
        'categories': {
            'type': 'list',
        },
    },
    'relations': [
        {
            'direction': 'to',
            'type': 'HAS_CITATION',
            'labels': ['Work'],
        },
        {
            'direction': 'to',
            'type': 'HAS_SOURCE',
            'labels': ['Work'],
        },
        {
            'direction': 'to',
            'type': 'HAS_TAG',
            'labels': ['Tag'],
        },
        {
            'direction': 'to',
            'type': 'IS_NEXT_ITERATION_OF',
            'labels': ['Record'],
        },
    ]
})

event_schema = combine(record_schema, {
    'labels': ['Event'],
    'properties': {
        'categories': {
            'type': 'list',
            'choices': [
                'course',
                'exhibition',
                'performance',
                'reception',
                'residency',
                'workshop',
            ]
        },
        'price_min': {
            'type': 'decimal',
        },
        'price_max': {
            'type': 'decimal',
        },
        'date_start': {
            'type': 'date',
            # 'default': now
        },
        'date_end': {
            'type': 'date',
        },
        'status': {
            'type': 'string',
            'choices': {
                'cancelled',
            },
        },
        'group_friendly': {
            'type': 'boolean',
        },
    },
    'relations': [
        {
            'direction': 'to',
            'type': 'HAS_VENUE',
            'labels': ['Place'],
        },
        {
            'direction': 'to',
            'type': 'ORGANIZED_BY',
            'labels': ['Person', 'Organization'],
        },
        {
            'direction': 'to',
            'type': 'PRODUCED_BY',
            'labels': ['Person', 'Organization'],
        },
        {
            'direction': 'to',
            'type': 'CONTRIBUTED_TO_BY',
            'labels': ['Person', 'Organization'],
        },
        {
            'direction': 'to',
            'type': 'PART_OF',
            'labels': ['Event'],
        },
    ],
})
