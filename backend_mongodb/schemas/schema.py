from lists.currencies import CURRENCIES
from lists.countries import COUNTRIES
from lists.languages import LANGUAGES

roles = [
    'member',
    'manager',
    'admin',
]

base_schema = {
    'name': {'type': 'string'},
    'synopsis': {'type': 'string'},
    'acls': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'required': True,
            'schema': {
                'role': {
                    'type': 'list',
                    'allowed': roles
                },
                'user': {
                    'type': 'string',
                    'data_relation': {
                        'resource': 'user',
                        'field': '_id',
                    }
                },
                'permissions': {
                    'type': 'dict',
                    'required': True,
                    'schema': {
                        'read': {
                            'type': 'boolean',
                            'default': True
                        },
                        'write': {
                            'type': 'boolean',
                            'default': False
                        }
                    }
                }
            }
        }
    }
}

contact_info_schema = {
    'phones': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'unique': True,
            'required': True,
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
            'unique': True,
            'required': True,
            'schema': {
                'category': {
                    'type': 'list',
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
    'addresses': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'unique': True,
            'required': True,
            'schema': {
                'category': {
                    'type': 'list',
                    'allowed': [
                        'personal',
                        'work'
                    ],
                    'default': 'personal'
                },
                'address': {
                    'type': 'string',
                    'data_relation': {
                        'resource': 'location',
                        'field': '_id',
                    },
                }
            }
        }
    }
}

rights_schema = {
    'copyright_owner': {
        'type': 'string',
        'default': 'the author',
    },
    'license': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'allowed': [
                    'all rights reserved',
                    'fair use',
                    'MIT',
                    'BSD',
                    'GPL',
                    'custom'
                ],
            },
            'url': {'type': 'string'}
        }
    }
}

approx_date_schema = {
    'date': {
        'type':'dict',
        'required': True,
        'unique': True,
        'schema': {
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
            },
            'approximate': {
                'type': 'boolean',
                'default': False
            }
        }
    }
}

approx_date_span_schema = {
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

identifiers_schema = {
    'id': {
        'type': 'dict',
        'required': True,
        'unique': True,
        'schema': {
            'category': {
                'type': 'string',
                'allowed': [
                    'slug',
                    'doi',
                    'isbn',
                    'call_number',
                    'ezid',
                ]
            },
            'value': {'type': 'string'}
        }
    }
}

hours_schema = {
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

users_schema = {
    **base_schema,
    **{
        'category': {
            'type': 'list',
            'required': True,
            'unique': True,
            'allowed': roles
        },
        'pass_hash': {'type': 'string'},
    }
}

locations_schema = {
    **base_schema,
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
        'street': {'type': 'string'},
        'city': {'type': 'string'},
        'state_province': {
            'type': 'string',
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

citations_schema = {
    'category': {
        'type': 'string',
        'required': True,
        'allowed': [
            'webpage',
            'book',
            'journal_article',
            'newspaper_article',
            'artwork',
            'archive_item',
        ]
    },
    'work': {
        'type': 'string',
        'required': True,
        'data_relation': {
            'resource': 'node',
            'field': '_id',
        }
    },
    'abstract': {'type': 'string'},
    'version': {'type': 'string'},
    'via': {
        'type': 'dict',
        'schema': {
            'archive': {
                'type': 'string',
                'required': True,
                'data_relation': {
                    'resource': 'node',
                    'field': '_id',
                },
            'accessed': {
                'type': 'datetime',
                'required': True,
            },
            'url': {'type': 'string'},
            'remote_id': {
                'type': 'string',
                'required': True,
                'data_relation': {
                    'resource': 'identifier',
                    'field': '_id',
                }
            },
        }
    },
    'rights': {
        'data_relation': {
            'resource': 'rights',
            'field': '_id',
        }
    },
    'notes': {'type': 'string'},
    }
}

nodes_schema = {
    **base_schema,
    **{
        'owner': {
            'type': 'string',
            'required': True,
            'data_relation': {
                'resource': 'user',
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
                'resource': 'tag',
                'field': '_id',
            },
        },
        'parent': {
            'type': 'string',
            'data_relation': {
                'resource': 'node',
                'field': '_id',
            },
        },
        'identifiers': {
            'type': 'list',
            'data_relation': {
                'resource': 'identifier',
                'field': '_id'
            }
        },
        'citations': citations_schema,
        "accounts": {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'service': {
                        'type': 'string',
                        'required': True,
                        'allowed': [
                            'Facebook',
                            'Twitter',
                            'Pinterest',
                        ],
                    },
                    'account': {
                        'type': 'string',
                        "required": True
                    }
                }
            }
        },
        "urls": {
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
                        'resource': 'location',
                        'field': '_id',
                    },
                },
                'bio': {'type': 'string'},
                'lifespan': {
                    'type': 'dict',
                    'schema': approx_date_span_schema
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
                    'type': 'list',
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
                'hourset': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'name': {'type': 'string'},
                            'hours': {
                                'type': 'dict',
                                'schema': {
                                    'monday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'hour_span',
                                            'field': '_id',
                                        }
                                    },
                                    'tuesday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'hour_span',
                                            'field': '_id',
                                        }
                                    },
                                    'wednesday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'hour_span',
                                            'field': '_id',
                                        }
                                    },
                                    'thursday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'hour_span',
                                            'field': '_id',
                                        }
                                    },
                                    'friday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'hour_span',
                                            'field': '_id',
                                        }
                                    },
                                    'saturday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'hour_span',
                                            'field': '_id',
                                        }
                                    },
                                    'sunday': {
                                        'type': 'string',
                                        'data_relation': {
                                            'resource': 'hour_span',
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
                    'type': 'list',
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
                        'website',
                        'object',
                        'article',
                        'serial',
                        'installation',
                    ]
                },
                'description': {'type': 'string'},
                'language': {
                    'type': 'string',
                    'allowed': list(LANGUAGES.keys()),
                },
                'book_data': {
                    'type': 'dict',
                    'schema': {
                        'series': {'type': 'string'},
                        'pages': {
                            'type': 'number',
                            'min': 1
                        },
                    }
                },
                'website_data': {
                    'type': 'dict',
                    'schema': {
                        'root_url': {'type': 'string'}
                    }
                },
                'article_data': {
                    'type': 'dict',
                    'schema': {
                        'volume': {'type': 'string'},
                        'series': {'type': 'string'},
                        'issue': {'type': 'string'},
                        'pages': {'type': 'string'},
                    }
                },
                'object_data': {
                    'type': 'dict',
                    'schema': {
                        'category': {
                            'type': 'list',
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
                                'acrylic on canvas',
                                'mixed media',
                            ]
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
                },
                'installation_data': {
                    'type': 'dict',
                    'schema': {
                        'location': {
                            'type': 'string',
                            'data_relation': {
                                'resource': 'node',
                                'field': '_id'
                            }
                        },
                        'timespan': {
                            'type': 'string',
                            'data_relation': {
                                'resource': 'timespan',
                                'field': '_id'
                            }
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
            'resource': 'node',
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

            # (org)-[*]->(work:artobject)
            'archive_of',

            # (org)-[*]->(work:event)
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
            'resource': 'node',
            'field': '_id',
        },
    },
    'properties': {
        'type': 'dict',
        'schema': {
            'timespan': {
                'type': 'dict',
                'schema': approx_date_span_schema
            }
        }
    }
}

collections_schema = {
    **base_schema,
    **{
        'node': {
            'type': 'list',
            'schema': {
                'type': 'string',
                'data_relation': {
                    'resource': 'node',
                    'field': '_id',
                }
            }
        }
    }
}

files_schema = {
    **base_schema,
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

tags_schema = {
    **base_schema,
    **{
        'synonyms': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'required': True,
                'unique': True,
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
            }
        }
    }
}

pages_schema = {
    **base_schema,
    **{
        'category': {
            'type': 'string',
            'required': True,
            'allowed': [
                'standard',
                'article',
            ]
        },
        'slug': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'body': {'type': 'string'}
    }
}
