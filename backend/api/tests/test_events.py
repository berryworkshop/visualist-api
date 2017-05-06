import requests
# import docker
import json
from unittest import TestCase
from urllib.parse import urljoin
from neomodel.core import StructuredNode
from ..app import app, config

class EventTestCase(TestCase):

    def setUp(self):
        self.api_base_url = 'http://neo4j:neo4j@localhost:5000/v1/'
        self.events_url = urljoin(self.api_base_url, 'events/')

        with open('{}/fixtures/events.json'.format(app.root_path)) as fixture:
            events = json.load(fixture)

        # client = docker.from_env()
        # client.containers.run("--publish=7474:7474 --publish=7687:7687 --volume= neo4j", detach=True, publish_all_ports=True, volumes=['$HOME/neo4j/data:/data'])

    def tearDown(self):
        # self.db.stop()
        pass

    def test_events_url_loads(self):
        # r = requests.get(self.events_url)
        # self.assertEqual(r.status_code, 200)
        pass

    def test_events_url_contains_objects(self):
        # r = requests.get(self.events_url)
        # self.assertTrue('objects' in r.json())
        pass

    def test_events_url_contains_all_objects(self):
        '''
        checking to make sure I have added links to all views
        '''
        pass
