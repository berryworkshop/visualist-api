schema = {
    'start': {'type': 'datetime'},
    'duration': {
        'type': 'dict',
        'schema': {
            'hours': {
                'type': 'number',
                'min': 0,
                'max': 23
            },
            'minutes': {
                'type': 'number',
                'min': 0,
                'max': 59
            },
        }
    }
}
