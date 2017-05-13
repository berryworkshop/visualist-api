import requests
# import docker
from unittest import TestCase
from urllib.parse import urljoin
from ..app import app

class EventTestCase(TestCase):

    def setUp(self):
        self.api_base_url = 'http://localhost:5000/'
        self.events_url = urljoin(self.api_base_url, 'events/')

        # client = docker.from_env()
        # client.containers.run("--publish=7474:7474 --publish=7687:7687 --volume= neo4j", detach=True, publish_all_ports=True, volumes=['$HOME/neo4j/data:/data'])

    def tearDown(self):
        # self.db.stop()
        pass

    def test_events_url_loads(self):
        r = requests.get(self.events_url)
        self.assertEqual(r.status_code, 200)

    def test_events_url_contains_objects(self):
        r = requests.get(self.events_url)
        self.assertTrue('objects' in r.json())


