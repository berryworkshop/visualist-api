from .etc import dates_schema

record_schema = {
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
  'snippets': {
    'type': 'list',
    'schema': {
      'type': 'dict',
      'schema': {
        'body': {
          'type': 'string',
        },
        'source': {
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
          'default': 1,
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
  },

  # 'urls': {
  #   'type': 'list',
  #   'schema': {
  #     'type': 'dict',
  #     'schema': {
  #       'label': {
  #         'type': 'string',
  #       },
  #       'description': {
  #         'type': 'string',
  #       },
  #       'href': {
  #         'type': 'string',
  #         'required': True
  #       }
  #     }
  #   }
  # },
  'same_as': {
    'type': 'list',
    'schema': {
      'type': 'dict',
      'schema': {
        'system': {
          'type': 'string',
          'required': True,
          'allowed': [
            'ISBN',
            'ISSN',
            'DOI',
            'ULAN',
          ]
        },
        'identifier': {
          'type': 'string',
          'required': True
        }
      }
    }
  },
  'dates': {
    'type': 'list',
    'schema': dates_schema
  },
  'note': {
      'type': 'string',
  },
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
  'version': {
    'type': 'string',
    'default': '1'
  },
}}


page_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'post',
      'allowed': [
        'article',
        'collection',
        'post',
        'review',
        'tour',
      ]
    }
  },
}}


event_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'exhibition',
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
      'default': 'artist',
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
  'names_extra': {
    'type': 'list',
    'schema': {
      'type': 'string'
    }
  },
}}


place_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'point',
      'allowed': [
        # locative
        'area',
        'point',

        # political
        'region',
        'neighborhood',
        'city',
        'county',
        'state',
        'country',

        # physical
        'building',
        'park',
        'plaza',

        # geographic
        'island',
      ]
    }
  },
  'location': {
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
  },
  'polygons': {
    'type': 'string'
  },
  'address': {
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
  },
}}


organization_schema = {**record_schema, **{
  'types': {
    'type': 'list',
    'required': True,
    'schema': {
      'type': 'string',
      'required': True,
      'default': 'gallery',
      'allowed': [
        'archive',
        'association',
        'company',
        'consortium',
        'foundation',
        'gallery',
        'library',
        'museum',
        'publisher',
        'school',
      ]
    }
  },
  'appointment_only': {
    'type': 'boolean',
    'default': False
  },
  'hours': {
    'type': 'string'
  }
}}
