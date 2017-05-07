import json
from unittest import TestCase
from ..app import app
from py2neo import Graph


class ImportExportTestCase(TestCase):

    def setUp(self):
        self.api_base_url = 'http://localhost:5000/'
        self.graph = Graph("bolt://0.0.0.0:7687/")

        with open('{}/fixtures/events.json'.format(app.root_path)) as fixture:
            self.json = json.load(fixture)


    def test_fixture_loaded(self):
        self.assertTrue(self.json)

    def test_fixture_contains_objects(self):
        self.assertTrue(self.json['objects'])

    def test_database_is_empty(self):
        query = "MATCH (a) RETURN a"
        cursor = self.graph.run(query)
        self.assertFalse(cursor.forward())
