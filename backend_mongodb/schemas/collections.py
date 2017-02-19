from schemas import base

schema = {
    **base.schema,
    **{
        'node': {
            'type': 'list',
            'schema': {
                'type': 'string',
                'data_relation': {
                    'resource': 'node',
                    'field': '_id',
                }
            }
        }
    }
}
