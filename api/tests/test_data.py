import os
import yaml
import json
import cerberus
from unittest import TestCase


class DataTestCase(TestCase):

    def setUp(self):
        data_dir = '{}/../data/'.format(os.path.dirname(__file__))

        schema_path  = '{}/schema.yaml'.format(data_dir)
        with open(schema_path, 'r') as schema:
            self.schema_raw=schema.read()
        self.schema = yaml.load(self.schema_raw)

        artists_path = '{}/formatted/artists.yaml'.format(data_dir)
        with open(artists_path, 'r') as artists:
            self.artists_raw=artists.read()
        self.artists = yaml.load(self.artists_raw)

        artists_bad_path = '{}/formatted/artists_bad.yaml'.format(data_dir)
        with open(artists_bad_path, 'r') as artists:
            self.artists_bad_raw=artists.read()
        self.artists_bad = yaml.load(self.artists_bad_raw)

    def tearDown(self):
        pass

    def test_schema_loads(self):
        self.assertTrue(self.schema_raw)

    def test_schema_converts_from_yaml(self):
        self.assertTrue(self.schema)

    def test_schema_contains_schemas(self):
        schema_names = ["BaseSchema", "RecordSchema", "PersonSchema"]
        schema_nonexistent = "AardvarkSchema"
        for n in schema_names:
            self.assertTrue(n in self.schema)
        self.assertFalse(schema_nonexistent in self.schema)

    def test_schemas_contain_inherited_keys(self):
        person_schema = self.schema['PersonSchema']
        keys = [
            "slug", "featured", "last_name"
        ]
        for k in keys:
            self.assertTrue(k in person_schema)

    def test_artists_load(self):
        self.assertTrue(self.artists_raw)

    def test_artists_converts_from_yaml(self):
        self.assertTrue(self.schema)

    def test_artists_contains_expected_artist(self):
        artist_slugs = ["berry-allan-james"]
        artist_slug_nonexistent = "flurgleblark"
        filtered = list(filter(
            lambda a: a['slug'] in artist_slugs, self.artists))
        self.assertTrue(filtered)
        filtered_nonexistent = list(filter(
            lambda a: a['slug'] == artist_slug_nonexistent, self.artists))
        self.assertFalse(filtered_nonexistent)

    def test_artists_validate(self):
        schema = self.schema['PersonSchema']
        validator = cerberus.Validator(schema)
        for artist in self.artists:
            self.assertTrue(validator.validate(artist))

    def test_bad_artists_dont_validate(self):
        schema = self.schema['PersonSchema']
        validator = cerberus.Validator(schema)
        for artist in self.artists_bad:
            self.assertFalse(validator.validate(artist))
