from unittest import TestCase
from ..models import BaseNode, RecordNode, EventNode
from ..models._schemas import base_schema, record_schema, event_schema


class ModelsTestCase(TestCase):

    def setUp(self):
        self.instances = [
            BaseNode(),
            RecordNode(),
            EventNode()
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

    def test_record_schema_has_all_labels(self):
        self.assertTrue('Base' in record_schema['labels'])
        self.assertTrue('Record' in record_schema['labels'])
        self.assertEqual(len(record_schema['labels']), 2)

    def test_event_schema_has_all_labels(self):
        self.assertTrue('Base' in event_schema['labels'])
        self.assertTrue('Record' in event_schema['labels'])
        self.assertTrue('Event' in event_schema['labels'])
        self.assertEqual(len(event_schema['labels']), 3)


    # def test_base_model_does_not_contain_child_model_labels(self):
    #     self.assertFalse('Record' in BaseNode().schema['labels'])
    #     self.assertFalse('Event' in BaseNode().schema['labels'])

    # def test_record_model_inherits_schema_labels(self):
    #     self.assertEqual(len(RecordNode().schema['labels']), 2)
    #     self.assertTrue('Base' in RecordNode().schema['labels'])
    #     self.assertTrue('Record' in RecordNode().schema['labels'])

    # def test_record_model_inherits_schema_properties(self):
    #     self.assertEqual(len(RecordNode().schema['properties']), 9)
    #     self.assertTrue(RecordNode().schema['properties']['slug'])
    #     self.assertTrue(RecordNode().schema['properties']['name'])

    # def test_record_model_inherits_schema_relations(self):
    #     self.assertEqual(len(RecordNode().schema['relations']), 4)

    # def test_property_types_exist_and_only_specified(self):
    #     for instance in self.instances:
    #         for k, v in instance.schema['properties'].items():
    #             try:
    #                 self.assertTrue(v['type'] in self.property_types)
    #             except Exception as e:
    #                 if v.get('type'):
    #                     raise AssertionError('not found: {}'.format(v['type'])) from e
    #                 else:
    #                     raise

    # def test_event_model_inherits_schema_labels(self):
    #     self.assertEqual(len(EventNode().schema['labels']), 3)
    #     self.assertTrue('Base' in EventNode().schema['labels'])
    #     self.assertTrue('Record' in EventNode().schema['labels'])
    #     self.assertTrue('Event' in EventNode().schema['labels'])

    # def test_event_model_inherits_schema_properties(self):
    #     # note: property "categories" is overridden in EventNode, on purpose
    #     self.assertEqual(len(EventNode().schema['properties']), 15)
    #     self.assertTrue(EventNode().schema['properties']['slug'])
    #     self.assertTrue(EventNode().schema['properties']['name'])
    #     self.assertTrue(EventNode().schema['properties']['price_min'])

    # def test_event_model_inherits_schema_relations(self):
    #     self.assertEqual(len(EventNode().schema['relations']), 9)

    # def test_record_created(self):
    #     record =

    # # def test_each_property_type(self):
    # #     pass
