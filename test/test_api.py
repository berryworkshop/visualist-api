from django.test import TestCase
from django.test import Client


class ApiRootTestCase(TestCase):
    def setUp(self):
        client = Client()
        self.response = client.get('/api/')

    def test_loads(self):
        '''Should load.'''
        self.assertTrue(self.response.content)

    def test_is_json(self):
        '''Should be json.'''
        self.assertTrue(self.response.json())

    def test_json_contains_links(self):
        '''Should have correct links.'''
        keys = [
            'groups',
            'records',
            'users',
        ]
        for key in keys:
            json = self.response.json()
            self.assertTrue(key in json)

