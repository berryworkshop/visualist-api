date_schema = {
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
        'accessed',
      ]
    },
    'date': {
      'type': 'string',
      'required': True
    },
  }
}

location_schema = {
  'type': 'dict',
  'schema': {
    'label': {
      'type': 'string',
      'default': 'occurred',
      'required': True,
      'allowed': [
        'born',
        'created',
        'died',
        'ended',
        'lived',
        'located',
        'occurred',
        'performed',
        'started',
      ]
    },
    'coordinates': {
      'type': 'list',
      'schema': {
        'type': 'dict',
        'schema': {
          'latitude': {
            'type': 'float',
            'required': True
          },
          'longitude': {
            'type': 'float',
            'required': True
          },
          'altitude': {
            'type': 'float'
          },
        }
      }
    },
    'addresses': {
      'type': 'list',
      'schema': {
        'type': 'dict',
        'schema': {
          'label': {
            'type': 'string',
          },
          'description': {
            'type': 'string',
          },
          'street': {
            'type': 'list',
            'required': True,
            'schema': {
              'type': 'string',
            }
          },
          'locality': {
            'type': 'string',
            'default': 'Chicago',
            'required': True,
          },
          'region': {
            'type': 'string',
            'required': True,
            'allowed': [
              'IL',
              'IN',
              'MI',
              'WI',
            ],
            'default': 'IL'
          },
          'postal_code': {
            'type': 'string'
          },
          'country': {
            'type': 'string',
            'allowed': [
              'US',
            ],
            'default': 'US',
            'required': True,
          }
        }
      }
    }
  }
}
