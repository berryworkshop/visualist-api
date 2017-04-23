schema = {
    "date": {
        "type":"dict",
        "required": true,
        "unique": true,
        "schema": {
            "year": {
                "type": "number",
                "required": true,
            },
            "month": {
                "type": "number",
                "required": false,
                "min": 1,
                "max": 12
            },
            "date": {
                "type": "number",
                "required": false,
                "dependencies": "month",
                "min": 1,
                "max": 31
            },
            "approximate": {
                "type": "boolean",
                "default": false
            }
        }
    }
}

span_schema = {
    "start": {
        "type": "string",
        "data_relation": {
            "resource": "approx_date",
            "field": "_id",
        }
    },
    "end": {
        "type": "string",
        "data_relation": {
            "resource": "approx_date",
            "field": "_id",
        }
    }
}
