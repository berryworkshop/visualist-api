import os
import requests
from py2neo import Graph
from base64 import b64encode
from unittest import TestCase
from ..project import app as visualist


class BaseTestCase(TestCase):

    def setUp(self):
        self.database_url = 'http://localhost:7474/db/data/'
        self.api_url = 'http://localhost:8000/'
        self.sub_views = [
            'events',
        ]
        self.graph = Graph(
            self.database_url, password='test_database_password')


    def tearDown(self):
        pass

    def test_api_loads(self):
        r = requests.get(self.api_url)
        self.assertEqual(r.status_code, 200)

    def test_database_loads_no_auth(self):
        r = requests.get(self.database_url)
        self.assertEqual(r.status_code, 401)

    def test_database_loads_with_auth(self):
        r = requests.get(self.database_url, auth=(
            'neo4j','test_database_password'))
        self.assertEqual(r.status_code, 200)

    def test_database_is_empty(self):
        r = self.graph.data("MATCH (a) RETURN a")
        self.assertFalse(r)

