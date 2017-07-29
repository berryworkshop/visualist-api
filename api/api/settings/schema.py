SnippetSchema = {
  'text': {
    'type': 'string',
    'required': True
  }
}
# relations:
#   - has_source (Work)
#   - has_license (License)
  
BaseSchema = {
  'slug': {
    'unique': True,
    'type': 'string',
    'required': True
  }
}
# relations:
#   - has_description (Snippet)
# calculated:
# - date
# - url

LicenseSchema = {**BaseSchema, **{
  'name': {
    'unique': True,
    'type': 'string'
  },
  'text': {
    'type': 'string'
  },
  'url': {
    'unique': True,
    'type': 'string',
    'required': True
  }
}}

UserSchema = {**BaseSchema, **{
  'username': {
    'type': 'string',
    'unique': True,
    'required': True
  },
  'password_hash': {
    'type': 'string',
    'required': True
  }
}}
# relations:
#   - has_role (Role)
#   - has_email (Email)
#   - same_as (Person)
#   - has_avatar (Image)
#   - has_permission (Permission)
#   - has_social_account (SocialAccount)
#   - has_favorite (Record)
#   - has_plans_to_visit (Record)
#     - status
#   - member_of (Organization)
#   - authored (Record)
#     - timestamp
#   - modified (Record)
#     - timestamp
# calculated:
#   - name

RecordSchema = {**BaseSchema, **{
  'name': {
    'type': 'string',
    'required': True
  },
  'description': {
    'type': 'string'
  },
  'featured': {
    'type': 'boolean',
    'default': False
  },
  'approved': {
    'type': 'boolean',
    'default': False
  },
  'public': {
    'type': 'boolean',
    'default': False
  },
  'categories': {
    'type': 'list',
    'schema': {
      'type': 'string'
    }
  },
  'same_as': {
    'type': 'string',
    'unique': True
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
}}
# relations
# - has_source (Work)
# - has_tag (Tag)
# - has_image (Image)
#   - aspect
#     - main
#     - detail
#     - recto
#     - verso
#     - signature
# - is_next_iteration_of (Record)
# calculated:
# - citation
# - date

WorkSchema = {**RecordSchema, **{
  'categories': {
    'type': 'list',
    'schema': {
      'type': 'string',
      'allowed': [
        'article',
        'book',
        'installation',
        'photograph',
        'sculpture',
        'visual artwork',
        'website'
      ]
    }
  },
  'work_date_created': {
    'type': 'datetime'
  },
  'work_date_modified': {
    'type': 'datetime'
  },
  'work_date_published': {
    'type': 'datetime'
  },
  'work_version': {
    'type': 'string'
  },
  'url': {
    'type': 'string'
  }
}}
# relations:
# - has_license (License)
# - created_at (Place)
# - located_at (Place)
# - created_by (Person/Organization)
# - part_of (Work)
# calculated:
# - date
# - distance

PageSchema = {**RecordSchema, **{
  'text': {
    'type': 'string'
  },
  'categories': {
    'type': 'list',
    'schema': {
      'type': 'string',
      'allowed': [
        'standard',
        'article',
        'review'
      ]
    }
  }
}}
# relations:
#   - child_of (Page/Collection)
# calculated:
#   - date
#   - same_as

CollectionSchema = {**RecordSchema, **{
  'categories': {
    'type': 'list',
    'schema': {
      'type': 'string',
      'allowed': [
        'standard',
        'tour'
      ]
    }
  }
}}
# relations:
#   - has_record (Record)
#   - child_of (Page/Collection)
# calculated:
#   - date
#   - same_as

TagSchema = {**RecordSchema, **{
  'categories': {
    'type': 'list',
    'schema': {
      'type': 'string',
      'allowed': [
        'genre',
        'medium',
        'period',
        'technique'
      ]
    }
  }
}}
# relations:
#   - vocabulary (Work)
#   - has_icon (Image)

EntitySchema = {**RecordSchema, **{
  'emails': {
    'type': 'list',
    'schema': {
      'type': 'dict',
      'schema': {
        'label': {
          'type': 'string',
          'required': True
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
}}

EventSchema = {**EntitySchema, **{
  'categories': {
    'allowed': [
      'course',
      'exhibition',
      'performance',
      'reception',
      'residency',
      'workshop'
    ]
  },
  'date_start': {
    'type': 'datetime'
  },
  'date_end': {
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
# relations:
#   - has_venue (Place)
#   - organized_by (Person/Organization)
#   - curated_by (Person/Organization)
#   - produced_by (Person/Organization)
#   - contributed_to_by (Person/Organization)
#   - exhibited_at_by (Person/Organization)
#   - part_of (Event)
# calculated:
#   - date
#   - duration
#   - distance

PersonSchema = {**EntitySchema, **{
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
  'categories': {
    'type': 'list',
    'schema': {
      'type': 'string',
      'allowed': [
        'artist',
        'writer',
        'architect',
        'filmmaker',
        'curator',
        'gallerist',
        'professor'
      ]
    }
  },
  'date_born': {
    'type': 'datetime'
  },
  'date_died': {
    'type': 'datetime'
  },
  'gender': {
    'type': 'string',
    'allowed': [
      'male',
      'female',
      'other'
    ]
  },
  'nationalities': {
    'type': 'list',
    'schema': {
      'type': 'string',
      'default': 'American'
    }
  }
}}
# relations:
#   - has_address (Place)
#   - has_email (Email)
#   - has_phone (Phone)
#   - has_social_account (SocialAccount)
#   - born_at (Place)
#   - died_at (Place)
#   - represented_by (Person/Organization)
#   - employed_by (Person/Organization)
#   - member_of (Organization)
#   - friend_of (Person)
#   - child_of (Person)
  
OrganizationSchema = {**EntitySchema, **{
  'categories': {
    'type': 'list',
    'schema': {
      'type': 'string',
      'allowed': [
        'archive',
        'association',
        'company',
        'consortium',
        'foundation',
        'library',
        'museum',
        'school'
      ]
    }
  },
  'date_founded': {
    'type': 'datetime'
  },
  'date_dissolved': {
    'type': 'datetime'
  },
  'nonprofit': {
    'type': 'boolean',
    'default': True
  },
  'appointment_only': {
    'type': 'boolean',
    'default': False
  },
  'hours': {
    'type': 'string'
  }
}}
# relations:
#   - has_address (Place)
#   - has_email (Email)
#   - has_logo (Image)
#   - has_phone (Phone)
#   - has_social_account (SocialAccount)
#   - founded_at (Place)
#   - founded_by (Person)
#   - member_of (Organization)
#   - part_of (Organization)
# calculated:
#   - distance
#   - date

PlaceSchema = {**EntitySchema, **{
  'categories': {
    'type': 'list',
    'schema': {
      'type': 'string',
      'allowed': [
        'spot',
        'area',
        'island',
        'neighborhood',
        'city',
        'county',
        'region',
        'state',
        'country'
      ]
    }
  },
  'location': {
    'type': 'point',
    'unique': True
  },
  'polygons': {
    'type': 'multipolygon'
  },
  'address': {
    'unique': True,
    'type': 'dict',
    'schema': {
      'street': {
        'type': 'string'
      },
      'locality': {
        'type': 'string',
        'default': 'Chicago'
      },
      'region': {
        'type': 'string',
        'default': 'IL'
      },
      'postal_code': {
        'type': 'string'
      },
      'country': {
        'type': 'string',
        'default': 'US'
      }
    }
  }
}}
# relations:
#   - part_of (Place)
# calculated:
#   - address
#   - geo
#   - distance


