from vocabularies.languages import LANGUAGES
from vocabularies.currencies import CURRENCIES
from schemas import base, approx_date, contact_info, citations

schema = {
    **base.schema,
    **{
        # 'owner': {
        #     'type': 'string',
        #     'required': True,
        #     'data_relation': {
        #         'resource': 'user',
        #         'field': '_id',
        #     },
        # },
        'category': {
            'type': 'list',
            'required': True,
            'allowed': [
                'person',
                'organization',
                'event',
                'work',
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
        # 'citations': {
        #     'type': 'list',
        #     'schema': {**citations.schema}
        # },
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
                # 'lifespan': {
                #     'type': 'dict',
                #     'schema': {**approx_date.span_schema}
                # },
                # 'contact_info': {
                #     'type': 'dict',
                #     'schema': {**contact_info.schema}
                # }
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
                # 'contact_info': {
                #     'type': 'dict',
                #     'schema': {**contact_info.schema}
                # },
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
                },
                'timespan': {
                    'type': 'string',
                    'data_relation': {
                        'resource': 'timespan',
                        'field': '_id'
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
