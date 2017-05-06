import docker
import requests
from unittest import TestCase
from ..app import app, config


class BaseTestCase(TestCase):
    '''
    base url should look like this:
    {
      "links": {
        "events": "/events/"
      }
    }
    '''

    def setUp(self):
        self.database_url = 'http://localhost:7687/'
        self.api_base_url = 'http://localhost:5000/v1/'

        # client = docker.from_env()
        # self.container = client.containers.run("neo4j",
        #     detach=True,
        #     ports={7474:7474, 7687:7687},
        #     volumes=['/Users/aljabear/neo4j/data:/data']
        # )
        # self.container.start()`

    def tearDown(self):
        # self.container.stop()
        pass

    def test_base_url_loads(self):
        r = requests.get(self.api_base_url)
        self.assertEqual(r.status_code, 200)
        # pass

    def test_database_loads(self):
        r = requests.get(self.database_url)
        self.assertEqual(r.status_code, 400)

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
