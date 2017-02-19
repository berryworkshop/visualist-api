from schemas import base
from vocabularies.countries import COUNTRIES

schema = {
    **base.schema,
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
