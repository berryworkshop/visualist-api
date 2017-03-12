from schemas import base
from vocabularies.roles import ROLES

schema = {
    **base.schema,
    **{
        'category': {
            'type': 'list',
            'required': True,
            'unique': True,
            'allowed': ROLES
        },
        'pass_hash': {'type': 'string'},
    }
}
