{
  "records": [{
    // "identifiers": [{
    //   "_t": "identifier",
    //   "_super": "<base>",
    //   "value": "XXXXX",
    //   "source": "<source_id>"
    // }],
    // "descriptions": [
    //   "<description_id>"
    // ],
    "relations": [{
      "_t": "relation",
      "_super": "<base>",
      "name": "located at",
      "value": "<record_id>",
      "timespan": "<approx_date_span_id>",
      "source": "<source_id>",
    }],
  }, {
    "_t": "person",
    "birthplace": "<place_id>",
    "lifespan": "<approx_date_span>",
    "aliases": [{
      "_t": "alias",
      "_super": "<base>",
      "name": "niteshade",
      "caption": "Old handle from high school.",
      "source": "<source_id>",
    }],
    "phones": [
      "<phone_id>"
    ],
    "addresses": [
      "<place_id>"
    ],
    "bio": "<description_id>",
    "user": "<user_id>"
  }, {
    "_t": "venue",
    "lifespan": "<approx_date_span>",
    "members": [{
      "_t": "member",
      "_super": "<base>",
      "role": "President",
      "value": "<body_id>",
      "timespan": "<approx_date_span_id>",
    }],
    "lifespan": "<timestamp_span_id>",
    "hours": [{
      "_t": "hours",
      "_super": "<base>",
      "name": "Summer hours",
      "timespan": "<timestamp_span_id>",
      "value": "<hour_set>"
    }],
    "place": "<place_id>"
  }, {
    "_t": "event",
    "_super": "<work>",
    "venue": "<venue_id>",
    "timespan": "<timestamp_span_id>",
    "prices": [{
      "_t": "price",
      "_super": "<base>",
      "amount": "12.00",
      "currency": "USD",
    }]
  }, {
    "_t": "work",
    "_super": "<work>",
    "name": "Les Demoiselles d'Avignon.",
    "medium": "oil on canvas",

    "mass": {
      "value": 12.34,
      "unit": "kg"
    },
    "values": [{
      "_t": "value",
      "_super": "<base>",
      "appraised_value": 1234.00,
      "currency": "USD",
      "appraisal": "<appraisal_id>",
    }]
  }, {
    "_t": "page",
    "_super": "<work>",
    "name": "About The Visualist",
    "caption": "This page tells all about The Visualist.",
    "body": "Lorem <span>ipsum</span>."
  }],
  "timestamp_spans": {
    "start": "2017-01-01T16:00:000-6:00",
    "end": "2017-03-01T00:00:000-6:00",
    "duration": "T1:23:48",
    "all_day:": false,
  },
  "approx_date_spans": {
    "start": "2017-01-01",
    "end": "~2017-03",
    "duration": "~2 months",
  },
  "approx_time_spans": {
    "start": "18:00:00",
    "end": "~26:00:00",
    "duration": "~8 hours"
  },
  "subjects": {
    "value": "library",
    "source": "<source_id>"
  },
  "descriptions": {
    "value": "Lorem ipsum dolor sit amet.",
    "source": "<source_id>"
  },
  "users": {
    "username": "allanberry",
    "password": "XXXXXXX",
    "groups": [
      "<group_id"
    ]
  },
  "groups": {
    "permissions": null
  },
  "collections": {
    "name": "My tour of Chicago.",
    "privacy_level": "<privacy_level>"
  },
  "privacy_levels": {
    "name": "public",
    "level": 0
  },
  "hour_sets": {
    "set": {
      "mon": ["<approx_time_span>"],
      "tue": ["<approx_time_span>"],
      "wed": ["<approx_time_span>"],
      "thu": ["<approx_time_span>"],
      "fri": ["<approx_time_span>"],
      "sat": ["<approx_time_span>"],
      "sun": ["<approx_time_span>"]
    }
  },
  "appraisals": {
    "appraiser": "<person_id>",
    "date": "2017-01-01",
  },
}
