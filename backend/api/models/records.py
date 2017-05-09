from .base import RecordModel


class EventModel(RecordModel):

    def __init__(self, *labels, **properties):
        super().__init__(*labels, **properties)
        schema = {
            'labels': ['Event'],
            'properties': {
                'categories': {
                    'type': 'list',
                    'choices': [
                        'course',
                        'exhibition',
                        'performance',
                        'reception',
                        'residency',
                        'workshop',
                    ]
                },
                'price_min': {
                    'type': 'decimal',
                },
                'price_max': {
                    'type': 'decimal',
                },
                'date_start': {
                    'type': 'date',
                    # 'default': now
                },
                'date_end': {
                    'type': 'date',
                },
                'status': {
                    'type': 'string',
                    'choices': {
                        'cancelled',
                    },
                },
                'group_friendly': {
                    'type': 'boolean',
                },
            },
            'relations': [
                # TODO
            ],
        }
        self.schema = super().combine_schemas(self.schema, schema)


    @property
    def citation(self):
        pass

    @property
    def date(self):
        pass
