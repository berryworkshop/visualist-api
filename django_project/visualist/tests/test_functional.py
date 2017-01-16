from django.core.urlresolvers import reverse, resolve
from django.test import TestCase, Client
from timeline.models import Event


class HomeTestCase(TestCase):
    '''
    Tests for the Home page.
    '''

    def setUp(self):
        self.url = reverse('home')
        self.response = self.client.get(self.url)

    def test_url(self):
        '''
        Ensure uses correct url.
        '''
        self.assertEqual(self.url, '/')

    def test_loads(self):
        '''
        Ensure loads OK.
        '''
        self.assertEqual(self.response.status_code, 200)

    def test_renders_strings(self):
        '''
        Ensures strings are present in response.
        '''
        fragments = [
            '<head>',
            '<body>',
            '<header>',
            '<main>',
            '<section id="ankle">',
            '<footer>',
        ]
        for f in fragments:
            self.assertContains(self.response, f, html=False)

    # def test_messages(self):
    #     fragment = '<section id="messages">'
    #     # self.assertContains(self.response, fragment, html=False)
    #     pass

    def test_renders_elements(self):
        '''
        Ensures elements are present in response.
        '''
        elements = [
            '<title>Visualist</title>',
        ]
        for e in elements:
            self.assertContains(self.response, e, html=True)

    def test_uses_templates(self):
        '''
        Ensures templates used by response.
        '''
        templates = [
            'visualist/home.html',
            'visualist/base.html',
        ]
        for t in templates:
            self.assertTemplateUsed(self.response, t)


class EventTestCase(TestCase):
    '''
    Tests for the Event page.
    '''

    def setUp(self):
        event = Event.objects.create(name='Test Event')
        self.url = reverse('event', args=[event.pk])
        self.response = self.client.get(self.url)

    def test_loads(self):
        '''
        Ensure loads OK.
        '''
        self.assertEqual(self.response.status_code, 200)