import requests
import app as visualist
from unittest import TestCase


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
        # self.database_url = 'http://0.0.0.0:7474/db/data/'
        # self.api_base_url = 'http://localhost:5000/'
        # self.sub_views = [
        #     'events',
        # ]

        visualist.configure_app(visualist.app)
        self.app = visualist.app.test_client()
        visualist.init_db()

        # Maybe someday I'll get docker running through Python
        # https://docs.docker.com/engine/reference/commandline/run/
        # client = docker.from_env()
        # docker run --rm -p 7474:7474 -p 7687:7687  -e 'NEO4J_AUTH=none' -v $HOME/neo4j/data:/data neo4j:3.1
        # self.container = client.containers.run("neo4j",
        #     detach=True,
        #     environment={'NEO4J_AUTH':'none'},
        #     ports={7474:7474, 7687:7687},
        #     volumes={'/Users/aljabear/neo4j/data': {'bind': '/data', 'mode': 'rw'}}
        # )
        # self.container.start()

    def tearDown(self):
        # visualist.stop_db(self.app)
        pass


    def test_base_url_loads(self):
        # r = requests.get(self.api_base_url)
        # self.assertEqual(r.status_code, 200)
        pass

    # def test_database_loads(self):
    #     r = requests.get(self.database_url)
    #     self.assertEqual(r.status_code, 200)

    # def test_base_url_contains_links(self):
    #     r = requests.get(self.api_base_url)
    #     self.assertTrue('links' in r.json())

    # def test_links_contains_events(self):
    #     r = requests.get(self.api_base_url)
    #     self.assertTrue('events' in r.json().get('links'))

    # def test_link_list_contains_all_views(self):
    #     r = requests.get(self.api_base_url)
    #     link_list = r.json().get('links')
    #     for v in self.sub_views:
    #         self.assertTrue(v in link_list)

    # def test_link_list_contains_same_number_of_views_as_sub_views(self):
    #     r = requests.get(self.api_base_url)
    #     link_list = r.json().get('links')
    #     self.assertEqual(len(self.sub_views), len(link_list))
