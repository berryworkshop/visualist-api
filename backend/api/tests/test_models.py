from unittest import TestCase
from ..models import BaseModel, RecordModel, EventModel


class ModelsTestCase(TestCase):

    def setUp(self):
        self.instances = [
            BaseModel(),
            RecordModel(),
            EventModel()
        ]
        self.property_types = [
            'boolean',
            'date',
            'date_time',
            'decimal',
            'dict',
            'email',
            'image',
            'integer',
            'integer_positive',
            'json',
            'list',
            'path',
            'slug',
            'string',
            'time',
            'url',
            'uuid',
        ]

        # self.property_arguments = [
        #     'blank',
        #     'default',
        #     'help_text',
        #     'max_length',
        #     'min_length',
        #     'options',
        #     'primary_key',
        #     'required',
        #     'schema',
        #     'type',
        #     'unique',
        #     'validators',
        # ]


    def tearDown(self):
        pass

    def test_base_model_does_not_contain_child_model_labels(self):
        self.assertFalse('Record' in BaseModel().schema['labels'])
        self.assertFalse('Event' in BaseModel().schema['labels'])

    def test_record_model_inherits_schema_labels(self):
        self.assertEqual(len(RecordModel().schema['labels']), 2)
        self.assertTrue('Base' in RecordModel().schema['labels'])
        self.assertTrue('Record' in RecordModel().schema['labels'])

    def test_record_model_inherits_schema_properties(self):
        self.assertEqual(len(RecordModel().schema['properties']), 9)
        self.assertTrue(RecordModel().schema['properties']['slug'])
        self.assertTrue(RecordModel().schema['properties']['name'])

    def test_record_model_inherits_schema_relations(self):
        self.assertEqual(len(RecordModel().schema['relations']), 4)

    def test_property_types_exist_and_only_specified(self):
        for instance in self.instances:
            for k, v in instance.schema['properties'].items():
                try:
                    self.assertTrue(v['type'] in self.property_types)
                except Exception as e:
                    if v.get('type'):
                        raise AssertionError('not found: {}'.format(v['type'])) from e
                    else:
                        raise

    def test_event_model_inherits_schema_labels(self):
        self.assertEqual(len(EventModel().schema['labels']), 3)
        self.assertTrue('Base' in EventModel().schema['labels'])
        self.assertTrue('Record' in EventModel().schema['labels'])
        self.assertTrue('Event' in EventModel().schema['labels'])

    def test_event_model_inherits_schema_properties(self):
        # note: property "categories" is overridden in EventModel, on purpose
        self.assertEqual(len(EventModel().schema['properties']), 15)
        self.assertTrue(EventModel().schema['properties']['slug'])
        self.assertTrue(EventModel().schema['properties']['name'])
        self.assertTrue(EventModel().schema['properties']['price_min'])

    def test_event_model_inherits_schema_relations(self):
        self.assertEqual(len(EventModel().schema['relations']), 4)

    # def test_each_property_type(self):
    #     pass
