import os
import yaml
import json
from unittest import TestCase


class DataTestCase(TestCase):

    def setUp(self):
        schema_path = '{}/../data/schema.yaml'.format(
            os.path.dirname(__file__))
        with open(schema_path, 'r') as schema:
            self.schema=schema.read()
        self.full_schema = yaml.load(self.schema)

    def tearDown(self):
        pass

    def test_schema_loads(self):
        self.assertTrue(self.schema)

    def test_converts_from_yaml(self):
        self.assertTrue(self.full_schema)

    def test_contains_schemas(self):
        schema_names = ["BaseSchema", "RecordSchema", "PersonSchema"]
        schema_nonexistent = "AardvarkSchema"
        for n in schema_names:
            self.assertTrue(n in self.full_schema)
        self.assertFalse(schema_nonexistent in self.full_schema)

    def test_schemas_contain_inherited_keys(self):
        person_schema = self.full_schema['PersonSchema']
        keys = [
            "slug", "featured", "last_name"
        ]
        for k in keys:
            self.assertTrue(k in person_schema)
