import requests
from unittest import TestCase
from urllib.parse import urljoin


class EventTestCase(TestCase):

    def setUp(self):
        self.api_base_url = 'http://localhost:5000/v1/'
        self.events_url = urljoin(self.api_base_url, 'events/')

    def tearDown(self):
        pass

    def test_events_url_loads(self):
        r = requests.get(self.events_url)
        self.assertEqual(r.status_code, 200)

    def test_events_url_contains_objects(self):
        r = requests.get(self.events_url)
        self.assertTrue('objects' in r.json())

    # def test_events_url_contains_all_objects(self):
    #     '''
    #     checking to make sure I have added links to all views
    #     '''
    #     r = requests.get(self.api_base_url)
    #     pass
