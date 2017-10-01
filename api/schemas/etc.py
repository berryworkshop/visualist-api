dates_schema = {
  'type': 'dict',
  'schema': {
    'label': {
      'type': 'string',
      'default': 'occurred',
      'required': True,
      'allowed': [
        'occurred',
        'started',
        'concluded',
      ]
    },
    'date': {
      'type': 'string',
      'required': True
    },
  }
}
