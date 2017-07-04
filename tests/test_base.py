import requests
from unittest import TestCase


class BaseTestCase(TestCase):

    def setUp(self):
        self.database_url = 'http://localhost:7474/db/data/'
        self.api_url = 'http://localhost:8000/'
        self.sub_views = [
            'events',
        ]

    def tearDown(self):
        pass

    def test_api_loads(self):
        r = requests.get(self.api_url)
        self.assertEqual(r.status_code, 200)

