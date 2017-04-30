import requests
from unittest import TestCase


class BaseTestCase(TestCase):

    def setUp(self):
        self.api_base_url = 'http://localhost:5000/v1/'

    def tearDown(self):
        pass

    def test_base_url_loads(self):
        r = requests.get(self.api_base_url)
        self.assertEqual(r.status_code, 200)

    # base url should look like this:
    # {
    #   "links": {
    #     "events": "/events/"
    #   }
    # }

    def test_base_url_contains_links(self):
        r = requests.get(self.api_base_url)
        self.assertTrue('links' in r.json())

    def test_links_contains_events(self):
        r = requests.get(self.api_base_url)
        self.assertTrue('events' in r.json().get('links'))

    def test_links_contains_all_views(self):
        '''
        checking to make sure I have added links to all views
        '''
        r = requests.get(self.api_base_url)
        link_list = r.json().get('links')
        sub_views = [
            'events',
        ]
        for v in sub_views:
            self.assertTrue(v in link_list)
