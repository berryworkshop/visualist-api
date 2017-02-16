base = {
    'created_by': {
        'type': 'string',
        'data_relation': {
            'resource': 'users',
            'field': '_id',
            'embeddable': False,
            'required': True,
        },
    },
    # 'language': {
    #     'type': 'string',
    #     'default': 'en-us',
    #     'allowed': [
    #         'en-us',
    #     ]
    # }
    # 'acls': [
    #   '<acl_id>'
    # ]
}

users = {
    'category': {
        'type': 'string',
        'required': True,
        'allowed': [
            'member',
            'manager',
            'admin',
        ]
    },
}

files = {
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
        'name': {'type': 'string'},
        'url': {'type': 'string'},
        'checksum': {'type': 'string'},
        # 'format': {
        #     'type': 'string',
        #     'required': True,
        #     'allowed': [
        #         '.tiff',
        #         '.gif',
        #         '.png',
        #         '.jpg',
        #         '.pdf',
        #     ]
        # },
        # 'aspect': {
        #     'type': 'string',
        #     'required': True,
        #     'allowed': [
        #         'main',
        #         'detail',
        #         'recto',
        #         'verso',
        #         'signature',
        #     ]
        # },
    }
}

records = {
    **base,
    **{
        'slug': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'name': {'type': 'string'},
        'caption': {'type': 'string'},
        'is_featured': {
            'type': 'boolean',
            'default': False,
        },
        'subjects': {
            'type': 'list',
            'data_relation': {
                'resource': 'terms',
                'field': '_id',
                'embeddable': False
            },
        },
        'sources': {
            'type': 'list',
            'data_relation': {
                'resource': 'sources',
                'field': '_id',
                'embeddable': False
            },
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
                        ]
                    },
                    'url': {'type': 'string'}
                }
            }
        },
        "websites": {
            'type': 'list',
            'schema': {
                'url': {
                    'type': 'string',
                    'required': True
                }
            }
        },
    }
}

people_organizations_shared = {
    **records,
    **{
        'related_works': {
            # separated because used by both people and organizations
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'person': {
                        'type': 'string'
                        'data_relation': {
                            'resource': 'works',
                            'field': '_id',
                            'embeddable': False,
                            'required': True,
                        },
                    },
                    'rel': {
                        'type': 'string',
                        'required': True,
                        'allowed': [
                            'creator_of',
                            'curator_of',
                            'owner_of',
                            'publisher_of',
                            'collector_of',
                        ]
                    }
                }
            }
        },
        'contact_info': {
            'type': 'dict',
            'schema': {
                'phones': {
                    'type': 'list',
                    # 'schema': {
                    #     'type': 'dict',
                    #     'schema': {
                    #         'category': {
                    #             'type': 'string',
                    #             'allowed': [
                    #                 'office',
                    #                 'mobile',
                    #             ]
                    #         }
                    #         'country': {'type': 'number'},
                    #         'area': {'type': 'number'},
                    #         'exchange': {'type': 'number'},
                    #         'number': {'type': 'number'},
                    #         'extension': {'type': 'number'},
                    #     }
                    # }
                },
                'emails': {
                    'type': 'list',
                    'schema': {
                        'email': {
                            'type': 'string',
                        }
                    }
                }
            }
        }
    }
}

people = {
    **people_organizations_shared,
    **{
        'name': {
            'type': 'dict',
            'schema': {
                'first': {'type': 'string'},
                'last': {
                    'type': 'string',
                    'required': True,
                },
            },
        },
        'related_people': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'person': {
                        'type': 'string'
                        'data_relation': {
                            'resource': 'people',
                            'field': '_id',
                            'embeddable': False,
                            'required': True,
                        },
                    },
                    'rel': {
                        'type': 'string',
                        'required': True,
                        'allowed': [
                            'friend_of',
                            'colleague_of',
                            'child_of',
                        ]
                    }
                }
            }
        },
        'related_organizations': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'person': {
                        'type': 'string'
                        'data_relation': {
                            'resource': 'organizations',
                            'field': '_id',
                            'embeddable': False,
                            'required': True,
                        },
                    },
                    'rel': {
                        'type': 'string',
                        'required': True,
                        'allowed': [
                            'member_of',
                        ]
                    }
                }
            }
        }
    }
}

organizations = {  # aka. venues
    **people_organizations_shared,
    **{
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
                'museum',
                'school',
            ]
        },
        'nonprofit': {
            'type': 'boolean',
            'default': True
        },
        'appointment_only': {
            'type': 'boolean',
            'default': False
        },
        'location': {
            'type': 'string',
            'data_relation': {
                'resource': 'locations',
                'field': '_id',
                'embeddable': False,
                'required': True,
            },
        }
        'related_people': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'person': {
                        'type': 'string'
                        'data_relation': {
                            'resource': 'works',
                            'field': '_id',
                            'embeddable': False,
                            'required': True,
                        },
                    },
                    'rel': {
                        'type': 'string',
                        'required': True,
                        'allowed': [
                            'exhibitor_of',
                            'employer_of',
                        ]
                    }
                }
            }
        },
        'related_organizations': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'person': {
                        'type': 'string'
                        'data_relation': {
                            'resource': 'organizations',
                            'field': '_id',
                            'embeddable': False,
                            'required': True,
                        },
                    },
                    'rel': {
                        'type': 'string',
                        'required': True,
                        'allowed': [
                            'department_of',
                            'member_of',
                        ]
                    }
                }
            }
        }
    }
}

works = {
    **records,
    **{
        'category': {
            'type': 'list',
            'required': True,
            'allowed': [
                'event',
                'thing',
                'page',
            ]
        },
        'related_works': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'person': {
                        'type': 'string'
                        'data_relation': {
                            'resource': 'works',
                            'field': '_id',
                            'embeddable': False,
                            'required': True,
                        },
                    },
                    'rel': {
                        'type': 'string',
                        'required': True,
                        'allowed': [
                            'part_of',
                        ]
                    }
                }
            }
        },
        'rights': {
            'type': 'dict',
            'schema': {
                'owner': {
                    'type': 'string',
                    'default': 'the author',
                }
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
                        }
                        'url': {'type': 'string'}
                    }
                }
            }
        }
        'book_md': {
            'type': 'dict',
            'schema': {
                'series': {'type': 'string'},
                'volume': {'type': 'string'},
                'number': {'type': 'string'},
                'page': {'type': 'string'},
            }
        },
        'physical_object_md': {
            'type': 'dict',
            'schema': {
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

locations = {
    **base,
    **{
        # 'category': {
        #     'type': 'string',
        #     'required': True,
        #     'allowed': [
        #         'place',
        #         'space',
        #     ]
        # },
        'name': {'type': 'string'}, # useful for cities, neighborhoods
        'caption': {'type': 'string'}, # ..
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
                'state': {'type': 'string'},
                'zip': {'type': 'string'},
                'state': {'type': 'string'},
                'country': {
                    'type': 'string',
                    'default': 'United States of America',
                    'allowed': [
                        'United States of America',
                        'Canada',
                        'Mexico',
                    ]
                }
            }
        }
    }
}

pages = {
    **records,
    **{
        'category': {
            'type': 'string',
            'required': True,
            'allowed': [
                'standard',
                'article',
            ]
        },
    }
}

terms = {
    **base,
    **{
        'category': {
            'type': 'string',
            'required': True,
            #   'allowed': [
            #     '???',
            #     '???',
            #   ]
        },
        'name': {'type': 'string'},
        'caption': {'type': 'string'},
        'sub_terms': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'term': {
                        'type': 'string'
                        'data_relation': {
                            'resource': 'terms',
                            'field': '_id',
                            'embeddable': False,
                            'required': True,
                        },
                    }
                }
            }
        }
        'synonyms': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'term': {'type': 'string'},
                    'vocabulary': {
                        'type': 'string',
                        'required': True,
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

citations = {
    **base,
    **{
        'work': {
            'type': 'string'
            'data_relation': {
                'resource': 'works',
                'field': '_id',
                'embeddable': False,
                'required': True,
            },
        },
        'accessed': {'type': 'datetime'},
        'section': {'type': 'string'},
        'comments': {'type': 'string'},
        # other one-off fields can go here
    }
}
