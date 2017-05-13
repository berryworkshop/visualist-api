'owner': {
    'type': 'string',
    'data_relation': {
        'resource': 'users',
        'field': '_id',
    },
},
'name': {'type': 'string'},
'synopsis': {'type': 'string'},
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
        'name': {'type': 'string'},
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
                ]
            },
            'url': {'type': 'string'},
        }
    }
},
"websites": {
    'type': 'list',
    'schema': {
        'url': {
            'type': 'string',
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
            'schema': {
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
                            'country': {'type': 'number'},
                            'area': {'type': 'number'},
                            'exchange': {'type': 'number'},
                            'number': {'type': 'number'},
                            'extension': {'type': 'number'},
                        }
                    }
                },
                'emails': {
                    'type': 'list',
                    'schema': {
                        'email': {
                            'type': 'string',
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
}
