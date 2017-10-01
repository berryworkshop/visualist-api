record_schema = {
  'name': {
    'type': 'string',
    'required': True
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
          'type': 'string'
        },
        'locality': {
          'type': 'string',
          'default': 'Chicago'
        },
        'region': {
          'type': 'string',
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
          'default': 'US'
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
  'identifiers': {
    'type': 'list',
    'schema': {
      'type': 'dict',
      'schema': {
        'system': {
          'type': 'string',
          'required': True,
          'allowed': [
            'ISBN',
            'DOI'
          ]
        },
        'value': {
          'type': 'string',
          'required': True
        }
      }
    }
  },
  'dates': {
    'type': 'list',
    'schema': {
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
        # 'circa': {
        #   'type': 'list',
        #   'schema': {
        #     'type': 'string',
        #     'allowed': [
        #       'Y', 'M', 'D'
        #     ]
        #   }
        # }
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

                # type
                # title

                # contributor
                #   type
                #     author
                #     editor
                #     translator
                #   name_first
                #   name_last

                # journal
                # issue
                # volume

                # id
                #   value
                #   type
                #     ISBN
                #     ISSN
                #     DOI

                # publication
                #   edition
                #   date
                #   publisher
                #   place

                # archive
                #   name
                #   place

                # online_source
                #   name
                #   URL
                #   accessed

                # newspaper
                #   section

                # abstract
                # note



  # 'date_created': { # in relation
  #   'type': 'date'
  # },
  # 'date_published': { # in relation
  #   'type': 'datetime'
  # },
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
  # 'names': {
  #   'type': 'list',
  #   'required': True,
  #   'schema': {
  #     'type': 'dict',
  #     'required': True,
  #     'schema': {
  #       'last': {
  #         'type': 'string',
  #         'required': True
  #       },
  #       'first': {
  #         'type': 'string'
  #       }
  #     }
  #   }
  # },
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
  }
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
  'centroid': {
    'type': 'point',
    # 'unique': True
  },
  'polygons': {
    'type': 'multipolygon'
  },
}}
