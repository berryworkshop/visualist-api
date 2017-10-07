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
  'note': {
      'type': 'string',
  },
}

work_schema = {**record_schema, **{
  'version': {
    'type': 'string',
    'default': '1'
  },
}}


event_schema = {**record_schema, **{
  'group_friendly': {
    'type': 'boolean',
    'required': True,
    'default': True
  }
}}


person_schema = {**record_schema, **{
  'names_extra': {
    'type': 'list',
    'schema': {
      'type': 'string'
    }
  },
}}

organization_schema = {**record_schema, **{
  'appointment_only': {
    'type': 'boolean',
    'default': False
  },
  'hours': {
    'type': 'string'
  }
}}


relation_schema = {
    'note': {
        'type': 'string',
    },
}

reference_schema = {**relation_schema, **{
    'section': {
        'type': 'string',
    },
    'place': {
        'type': 'string',
    },
    'url': {
        'type': 'string',
    },
    'journal': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
            },
            'issue': {
                'type': 'string',
            },
            'volume': {
                'type': 'string',
            },
        }
    },
    'archive': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
            },
            'place': {
                'type': 'string',
            },
            'url': {
                'type': 'string',
            },
            'accessed': {
                'type': 'datetime',
            }
        }
    }
}}

source_schema = {
    'authors': {
        'type': 'list',
        'schema': {
            'type': 'string',
        }
    },
    'editors': {
        'type': 'list',
        'schema': {
            'type': 'string',
        }
    },
    'translators': {
        'type': 'list',
        'schema': {
            'type': 'string',
        }
    },
        'collection_title': {
        'type': 'string',
    },
    'identifiers': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'system': {
                    'type': 'string',
                    'allowed': [
                        'ISBN',
                        'ISSN',
                        'DOI',
                    ]
                },
                'value': {
                    'type': 'string',
                }
            }
        }
    },
    'archive': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'required': True
            },
            'call_no': {
                'type': 'string',
            },
            'location_in_archive': {
                'type': 'string',
            },
        }
    },
    'edition': {
        'type': 'string',
    },
    'pages': {
        'type': 'string',
    },
    'volume': {
        'type': 'string',
    },
    'series': {
        'type': 'string',
    },
}

record_source_schema = {
    'pages': {
        'type': 'string',
    },
    'section': {
        'type': 'string',
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
}
