import sys
import requests
from py2neo import Graph
from unittest import TestCase


class DBTestCase(TestCase):

    def setUp(self):
        self.database_url = 'http://localhost:7474/db/data/'
        self.sub_views = [
            'events',
        ]
        self.graph = Graph(
            self.database_url, password='test_database_password')

        # Ensure database empty, otherwise clear in tearDown!
        r = self.graph.data("MATCH (a) RETURN a")
        try:
            self.assertFalse(r)
        except(AssertionError):
            print('Test database is not empty! Aborting!')
            self.fail()

    def tearDown(self):
        # Clear database!
        self.graph.data('MATCH (n) DETACH DELETE n')

    def test_database_loads_no_auth(self):
        r = requests.get(self.database_url)
        self.assertEqual(r.status_code, 401)

    def test_database_loads_with_auth(self):
        r = requests.get(self.database_url, auth=(
            'neo4j','test_database_password'))
        self.assertEqual(r.status_code, 200)


