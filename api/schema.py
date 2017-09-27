RecordSchema = {
  'name': {
    'type': 'string',
    'required': True
  },
  'description': {
    'type': 'string'
  },
  'categories': {
    'type': 'list',
    'schema': {
      'type': 'string'
    }
  },
  'identifiers': {
    'type': 'dict',
    'unique': True,
    'schema': {
      'vocabulary': {
        'type': 'string',
        'required': True,
        'allowed': [
          'AAT',
          'ULAN',
          'LCCN',
          'VIAF'
        ]
      },
      'value': {
        'type': 'string',
        'required': True
      }
    }
  }
  'urls': {
    'type': 'list',
    'schema': {
      'type': 'dict',
      'schema': {
        'label': {
          'type': 'string',
        },
        'description': {
          'type': 'string',
        }
        'href': {
          'type': 'string',
          'required': True
        }
      }
    }
  },
  'emails': {
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
        'address': {
          'required': True,
          'unique': True,
          'type': 'string'
        }
      }
    }
  },
  'phones': {
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
        'country': {
          'type': 'integer',
          'required': True
        },
        'area_code': {
          'type': 'integer',
          'required': True
        },
        'exchange_code': {
          'type': 'integer',
          'required': True
        },
        'number': {
          'type': 'integer',
          'required': True
        },
        'extension': {
          'type': 'integer'
        }
      }
    }
  },
  'social': {
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
        'service': {
          'required': True,
          'type': 'string',
          'allowed': [
            'Ask.fm',
            'Facebook',
            'Flickr',
            'Foursquare',
            'GitHub',
            'Google+',
            'Instagram',
            'LinkedIn',
            'Meetup',
            'Pinterest',
            'Reddit',
            'SnapChat',
            'Tumblr',
            'Twitter',
            'Vine',
            'WhatsApp',
            'Yelp',
            'YouTube'
          ]
        },
        'account': {
          'required': True,
          'type': 'string'
        }
      }
    }
  }
}

WorkSchema = {**RecordSchema, **{
  'date_created': {
    'type': 'date'
  },
  'date_published': {
    'type': 'datetime'
  },
  'version': {
    'type': 'string'
  },
}}


PageSchema = {**RecordSchema, **{
  'body': {
    'type': 'string'
  },
}}


EventSchema = {**RecordSchema, **{
  'datetime_start': {
    'type': 'datetime'
  },
  'datetime_end': {
    'type': 'datetime'
  },
  'status': {
    'default': 'OK',
    'required': True,
    'allowed': [
      'OK',
      'cancelled'
    ]
  },
  'group_friendly': {
    'type': 'boolean',
    'required': True,
    'default': True
  }
}}


PersonSchema = {**RecordSchema, **{
  'name': {
    'type': 'dict',
    'required': True,
    'schema': {
      'last': {
        'type': 'string',
        'required': True
      },
      'first': {
        'type': 'string'
      }
    }
  },
  'date_born': {
    'type': 'datetime'
  },
  'date_died': {
    'type': 'datetime'
  },
}}


OrganizationSchema = {**RecordSchema, **{
  'date_founded': {
    'type': 'datetime'
  },
  'date_dissolved': {
    'type': 'datetime'
  },
  'appointment_only': {
    'type': 'boolean',
    'default': False
  },
  'hours': {
    'type': 'string'
  }
}}


PlaceSchema = {**RecordSchema, **{
  'location': {
    'type': 'point',
    'unique': True
  },
  'polygons': {
    'type': 'multipolygon'
  },
}}
