record_schema = {
  'name': {
    'type': 'string',
    'required': True
  },
  'description': {
    'type': 'string'
  },
  'identifiers': {
    'type': 'dict',
    # 'unique': True,
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
  },
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
        },
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
        #   'unique': True,
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

work_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'artwork',
      'allowed': [
        'article',
        'artwork',
        'book',
        'installation',
        'license',
        'photograph',
        'sculpture',
        'vocabulary',
        'website',
      ]
    }
  },
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


page_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'Post',
      'allowed': [
        'article',
        'collection',
        'post',
        'review',
        'tour',
      ]
    }
  },
  'body': {
    'type': 'string'
  },
}}


event_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'Exhibition',
      'allowed': [
        'course',
        'convention',
        'exhibition',
        'fair',
        'performance',
        'reception',
        'residency',
        'workshop',
      ]
    }
  },
  'datetime_start': {
    'type': 'datetime'
  },
  'datetime_end': {
    'type': 'datetime'
  },
  'group_friendly': {
    'type': 'boolean',
    'required': True,
    'default': True
  }
}}


person_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'Artist',
      'allowed': [
        'architect',
        'artist',
        'curator',
        'filmmaker',
        'gallerist',
        'manager',
        'professor',
        'programmer',
        'writer',
      ]
    }
  },
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


organization_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'Gallery',
      'allowed': [
        'archive',
        'association',
        'company',
        'consortium',
        'foundation',
        'gallery',
        'library',
        'museum',
        'school',
      ]
    }
  },
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


place_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'Location',
      'allowed': [
        'area',
        'city',
        'country'
        'county',
        'island',
        'location',
        'neighborhood',
        'region',
        'state',
      ]
    }
  },
  'location': {
    'type': 'point',
    # 'unique': True
  },
  'polygons': {
    'type': 'multipolygon'
  },
}}
