from django.test import TestCase
from api.models import Resource


class ResourceTestCase(TestCase):
    def setUp(self):
        Resource.objects.create(
            title="lion",
            description="A lion roars.",
            url="http://example.com/lion")
        Resource.objects.create(
            title="cat",
            description="A cat meows.",
            url="http://example.com/cat")

    def test_resource_str(self):
        '''Resources are correctly converted to string.'''
        lion = Resource.objects.get(title="lion")
        cat = Resource.objects.get(title="cat")
        self.assertEqual(str(lion), 'lion')
        self.assertEqual(str(cat), 'cat')
