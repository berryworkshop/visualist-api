from lists.currencies import CURRENCIES
from lists.countries import COUNTRIES

contact_info_schema = {
    'phones': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'category': {
                    'type': 'string',
                    'required': False,
                    'allowed': [
                        'office',
                        'mobile',
                    ]
                },
                'country': {
                    'type': 'number',
                    'required': True,
                    'default': 1
                },
                'area': {
                    'type': 'number',
                    'required': True
                },
                'exchange': {
                    'type': 'number',
                    'required': True
                },
                'number': {
                    'type': 'number',
                    'required': True
                },
                'extension': {
                    'type': 'number',
                    'required': False
                },
            }
        }
    },
    'emails': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'category': {
                    'type': 'string',
                    'allowed': [
                        'personal',
                        'work'
                    ],
                    'default': 'personal'
                },
                'email': {
                    'type': 'string',
                }
            }
        }
    },
    'location': {
        'type': 'string',
        'data_relation': {
            'resource': 'locations',
            'field': '_id',
        },
    }
}

# rights_schema = {
#     'copyright_owner': {
#         'type': 'string',
#         'default': 'the author',
#     },
#     'license': {
#         'type': 'dict',
#         'schema': {
#             'name': {
#                 'type': 'string',
#                 'allowed': [
#                     'all rights reserved',
#                     'fair use',
#                     'MIT',
#                     'BSD',
#                     'GPL',
#                     'custom'
#                 ],
#             },
#             'url': {'type': 'string'}
#         }
#     }
# }

base = {
    'name': {'type': 'string'},
    'synopsis': {'type': 'string'},
    # 'acls': [
    #   '<acl_id>'
    #       "privacy_levels": {
    #         "name": "public",
    #         "level": 0
    #       },
    # ]
}


approx_dates = {
    **base,
    **{
        'year': {
            'type': 'number',
            'required': True,
        },
        'month': {
            'type': 'number',
            'required': False,
            'min': 1,
            'max': 12
        },
        'date': {
            'type': 'number',
            'required': False,
            'dependencies': 'month',
            'min': 1,
            'max': 31
        }
        'approximate': {
            'type': 'boolean',
            'default': False
        }
    }
}

approx_date_spans = {
    'start': {
        'type': 'string',
        'data_relation': {
            'resource': 'approx_date',
            'field': '_id',
        }
    },
    'end': {
        'type': 'string',
        'data_relation': {
            'resource': 'approx_date',
            'field': '_id',
        }
    }
}

# datetime_spans = {
#     'start': {'type': 'datetime'},
#     'end': {'type': 'datetime'},
#     'all_day': {
#         'type': 'boolean',
#         'default': False,
#     }
# }

users_schema = {
    **base,
    **{
        'category': {
            'type': 'string',
            'required': True,
            'allowed': [
                'member',
                'manager',
                'admin',
            ]
        },
        'pass_hash': {'type': 'string'},
    }
}

nodes_schema = {
    **base,
    **{
        'owner': {
            'type': 'string',
            'required': True,
            'data_relation': {
                'resource': 'users',
                'field': '_id',
            },
        },
        'category': {
            'type': 'list',
            'required': True,
            'allowed': [
                'person',
                'organization',
                'event',
                'work',
                'page',
            ]
        },
        'slug': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'is_featured': {
            'type': 'boolean',
            'default': False,
        },
        'tags': {
            'type': 'list',
            'data_relation': {
                'resource': 'tags',
                'field': '_id',
            },
        },
        'sources': {
            'type': 'dict',
            'schema': {
                'name': {
                    'type': 'string',
                    'default': 'original work'
                    },
                'remote_id': {'type': 'string'},
                'url': {'type': 'string'},
                'accessed': {'type': 'datetime'},
                'comments': {'type': 'string'},
            }
        },
        "accounts": {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'service': {
                        'type': 'string',
                        'allowed': [
                            'Facebook',
                            'Twitter',
                            'Pinterest',
                        ],
                        "required": True
                    },
                    'account': {
                        'type': 'string'
                        "required": True
                    },
                }
            }
        },
        "websites": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "name": {"type": "string"},
                    "url": {
                        "type": "string",
                        "required": True
                    }
                }
            }
        },
        'person_data': {
            'type': 'dict',
            'schema': {
                'name': {
                    'type': 'dict',
                    'schema': {
                        'first': {
                            'type': 'string'
                        },
                        'last': {
                            'type': 'string',
                            'required': True,
                        },
                    },
                },
                'birthplace': {
                    'type': 'string',
                    'data_relation': {
                        'resource': 'locations',
                        'field': '_id',
                    },
                },
                'bio': {'type': 'string'},
                'lifespan': {
                    'type': 'string',
                    'data_relation': {
                        'resource': 'approx_date_span',
                        'field': '_id',
                    },
                },
                'contact_info': {
                    'type': 'dict',
                    'schema': contact_info_schema
                }
            }
        },
        'organization_data': {
            'type': 'dict',
            'schema': {
                'category': {
                    'type': 'string',
                    'required': True,
                    'allowed': [
                        'gallery',
                        'museum',
                        'school',
                        'consortium',
                        'archive',
                        'association',
                        'company',
                        'foundation',
                        'library',
                        'museum',
                        'school',
                    ],
                },
                'description': {'type': 'string'},
                'nonprofit': {
                    'type': 'boolean',
                    'default': True
                },
                'appointment_only': {
                    'type': 'boolean',
                    'default': False
                },
                'contact_info': {
                    'type': 'dict',
                    'schema': contact_info_schema
                },
                'hours': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'name': {'type': 'string'},
                            'timespan': {
                                'type': 'string',
                                'data_relation': {
                                    'resource': 'datetime_spans',
                                    'field': '_id',
                                }
                            },
                            'hours': {
                                'type': 'dict',
                                'schema': {
                                    'monday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'datetime_spans',
                                            'field': '_id',
                                        }
                                    },
                                    'tuesday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'datetime_spans',
                                            'field': '_id',
                                        }
                                    },
                                    'wednesday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'datetime_spans',
                                            'field': '_id',
                                        }
                                    },
                                    'thursday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'datetime_spans',
                                            'field': '_id',
                                        }
                                    },
                                    'friday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'datetime_spans',
                                            'field': '_id',
                                        }
                                    },
                                    'saturday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'datetime_spans',
                                            'field': '_id',
                                        }
                                    },
                                    'sunday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'datetime_spans',
                                            'field': '_id',
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        'event_data': {
            'type': 'dict',
            'schema': {
                'category': {
                    'type': 'string',
                    'required': True,
                    'allowed': [
                        'exhibition',
                        'performance',
                        'reception',
                    ],
                },
                'description': {'type': 'string'},
                'prices': {
                    'type': 'dict',
                    'schema': {
                        'amount': {'type': 'number'},
                        'currency': {
                            'type': 'string',
                            'allowed': list(CURRENCIES.keys())
                        },
                    }
                }
            }
        },
        'work_data': {
            'type': 'dict',
            'schema': {
                'category': {
                    'type': 'string',
                    'required': True,
                    'allowed': [
                        'book',
                        'artobject',
                        'website',
                        'installation',
                    ]
                },
                'book_data': {
                    'type': 'dict',
                    'schema': {
                        'series': {'type': 'string'},
                        'pages': {'type': 'string'},
                    }
                },
                'artobject_data': {
                    'type': 'dict',
                    'schema': {
                        'category': {
                            'type': 'string',
                            'required': True,
                            'allowed': [
                                'painting',
                                'drawing',
                                'sculpture',
                                'installation',
                            ]
                        },
                        "medium": {
                            'type': 'string',
                            'allowed': [
                                'oil on canvas',
                                'acrylic on canvas'
                                'mixed media',
                            ]
                        },
                    }
                },
                'size': {
                    'type': 'dict',
                    'schema': {
                        'height': {'type': 'number'},
                        'width': {'type': 'number'},
                        'depth': {'type': 'number'},
                        'unit': {
                            'type': 'string',
                            'allowed': [
                                'in',
                                'ft',
                                'mm',
                                'cm',
                                'm',
                            ]
                        }
                    }
                }
            }
        }
    }
}

edges_schema = {
    'subject': {
        'type': 'string',
        'required': True,
        'data_relation': {
            'resource': 'nodes',
            'field': '_id',
        },
    },
    'predicate': {
        'type': 'string',
        'required': True,
        'allowed': [
            # (org)-[*]->(person)
            'exhibitor_of',
            'employer_of',

            # (person)-[*]->(person)
            'friend_of',
            'colleague_of',
            'child_of',

            # (person|org)-[*]->(org)
            'department_of',
            'member_of',

            # (person|org)-[*]->(work)
            'creator_of',
            'contributor_to',
            'author_of',
            'owner_of',
            'publisher_of',
            'collector_of',

            # (person)-[*]->(work)
            'curator_of',

            # (org)-[*]->(work)
            'venue_for',

            # (work)-[*]->(work)
            'source_for',
            'part_of',

            # (org)-[*]->(work)
            'department_of',
        ]
    },
    'object': {
        'type': 'string',
        'required': True,
        'data_relation': {
            'resource': 'nodes',
            'field': '_id',
        },
    },
    'properties': {
        'type': 'dict',
        'schema': {
            'timespan': {
                'type': 'string',
                'data_relation': {
                    'resource': 'approx_date_span',
                    'field': '_id',
                }
            }
        }
    }
}

collections_schema = {
    **base,
    **{
        'nodes': {
            'type': 'list',
            'schema': {
                'type': 'string',
                'data_relation': {
                    'resource': 'nodes',
                    'field': '_id',
                }
            }
        }
    }
}

files_schema = {
    **base,
    **{
        'category': {
            'type': 'string',
            'required': True,
            'allowed': [
                'image',
                'video',
                'document',
            ]
        },
        'url': {'type': 'string'},
        'checksum': {'type': 'string'},
        'image_data': {
            'type': 'dict',
            'schema': {
                "format": {
                    'type': 'string',
                    'allowed': [
                        '.tiff'
                        '.gif',
                        '.png',
                        '.jpg',
                        '.pdf',
                    ]
                },
                'aspect': {
                    'type': 'string',
                    'allowed': [
                        'main',
                        'detail',
                        'recto',
                        'verso',
                        'signature',
                    ]
                }
            }
        },
        'document_data': {
            'type': 'dict',
            'schema': {
                "format": {
                    'type': 'string',
                    'allowed': [
                        '.pdf',
                        '.doc',
                    ]
                }
            }
        }
    }
}

locations_schema = {
    **base,
    **{
        'category': {
            'type': 'string',
            'required': True,
            'default': 'place',
            'allowed': [
                'place',
                'neighborhood',
                'city',
            ]
        },
        'coordinates': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'longitude': {
                        'type': 'number',
                        'required': True,
                    },
                    'latitude': {
                        'type': 'number',
                        'required': True,
                    },
                    'altitude': {
                        'type': 'number',
                        'required': False,
                    }
                }
            }
        },
        'address': {
            'type': 'dict',
            'schema': {
                'street': {'type': 'string'},
                'city': {'type': 'string'},
                'state_province': {
                    'type': 'string'
                    'allowed': [
                        'IL',
                        'WI',
                        'IN',
                        'MI'
                    ]
                },
                'postal_code': {'type': 'string'},
                'country': {
                    'type': 'string',
                    'default': 'USA',
                    'allowed': list(COUNTRIES.keys()),
                }
            }
        }
    }
}

tags_schema = {
    **base,
    **{
        'synonyms': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'term': {'type': 'string'},
                    'vocabulary': {
                        'type': 'string',
                        'allowed': [
                            'Getty Art & Architecture Thesaurus',
                            'Library of Congress Subject Headings',
                        ]
                    },
                    'id': {'type': 'string'},
                    'url': {'type': 'string'},
                }
            },
        },
    }
}

pages_schema = {
    **base,
    **{
        'type': 'dict',
        'schema': {
            'category': {
                'type': 'string',
                'required': True,
                'allowed': [
                    'standard',
                    'article',
                ]
            },
            'body': {'type': 'string'}
        }
    }
}
