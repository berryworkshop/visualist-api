from schemas import approx_date

schema = {
    'subject': {
        'type': 'string',
        'required': True,
        'data_relation': {
            'resource': 'node',
            'field': '_id',
        },
    },
    'predicate': {
        'type': 'string',
        'required': True,
        'allowed': [
            # (org)-[*]->(person)
            'exhibitor_of',
            'employer_of',

            # (person)-[*]->(person)
            'friend_of',
            'colleague_of',
            'child_of',

            # (org)-[*]->(org)
            'department_of',

            # (person|org)-[*]->(org)
            'member_of',

            # (person|org)-[*]->(work)
            'creator_of',
            'contributor_to',
            'author_of',
            'owner_of',
            'publisher_of',
            'collector_of',

            # (person)-[*]->(work)
            'curator_of',

            # (org)-[*]->(work:artobject)
            'archive_of',

            # (org)-[*]->(work:event)
            'venue_of',

            # (work)-[*]->(work)
            'source_of',
            'part_of',

        ]
    },
    'object': {
        'type': 'string',
        'required': True,
        'data_relation': {
            'resource': 'node',
            'field': '_id',
        },
    },
    'properties': {
        'type': 'dict',
        'schema': {
            'timespan': {
                'type': 'dict',
                'schema': {**approx_date.span_schema}
            }
        }
    }
}
