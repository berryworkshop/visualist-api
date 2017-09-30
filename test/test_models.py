from django.test import TestCase
from api.models import Record
from django.core.exceptions import ValidationError


class RecordTestCase(TestCase):
    fixtures = ['api/fixtures/test_basic.json',]

    def setUp(self):
        Record.objects.create(
            slug="party",
            label="event",
            properties={
                "name": "Party",
                "types": [
                    "reception"
                ]
            }
        )
        Record.objects.create(
            slug="exhibition",
            label="event",
            properties={
                "name": "Exhibition",
                "types": [
                    "exhibition"
                ]
            }
        )
        Record.objects.create(
            slug="berry-allan",
            label="person",
            properties={
                "name": {
                    "first": "Allan James",
                    "last": "Berry"
                },
                "types": [
                    "artist",
                    "programmer"
                ]
            }
        )

    def test_record_name(self):
        '''Records are correctly converted to string.'''
        party = Record.objects.get(
            slug="party")
        allan = Record.objects.get(
            slug="berry-allan")
        self.assertEqual(party.name(), 'Party')
        self.assertEqual(allan.name(), 'Berry, Allan James')


    def test_record_str(self):
        '''Records are correctly converted to string.'''
        party = Record.objects.get(
            slug="party")
        exhibition = Record.objects.get(
            slug="exhibition")
        self.assertEqual(str(party), 'event: Party')
        self.assertEqual(str(exhibition), 'event: Exhibition')

    def test_bad_json(self):
        '''Bad records do not validate.'''
        badjson = {
            "this is": "a test" # does not have required fields
        }
        with self.assertRaises(ValidationError):
            Record.objects.create(
                slug="badrecord",
                label="event",
                properties=badjson
            )
            badrecord = Record.objects.get(
                slug="badrecord")

    def test_good_json(self):
        '''Good records validate OK.'''
        goodjson = {
            "name": "A great exhibition",
            "types": ["exhibition"]
        }
        Record.objects.create(
            slug="goodrecord",
            label="event",
            properties=goodjson
        )
        goodrecord = Record.objects.get(
            slug="goodrecord")
        self.assertTrue(goodrecord)
