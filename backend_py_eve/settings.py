from schemas import (
    nodes, edges, collections, users, files, locations, tags, pages)

# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'visualist'
API_VERSION = 'v1'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
AUTO_CREATE_LISTS = True

# development only
XML = False
IF_MATCH = False
X_DOMAINS = '*'
headers = [
    'Content-Type',
]
X_HEADERS = headers
X_EXPOSE_HEADERS = headers


node_base_projection = {
    'category': 1,
    'slug': 1,
    'name': 1,
}

DOMAIN = {
    'nodes': {
        # 'additional_lookup': {
        #     'url': 'regex("[-\w]+")',
        #     'field': 'slug'
        # },
        'schema': {**nodes.schema}
    },
    'events': {
        'datasource': {
            'source': 'nodes',
            # 'projection': {**node_base_projection},
            'filter': {
                'category': {'$eq': 'event'}
            }
        }
    },
    # 'people': {
    #     'datasource': {
    #         'source': 'nodes',
    #         # 'projection': {**node_base_projection},
    #         'filter': {
    #             'category': {'$eq': 'person'}
    #         }
    #     }
    # },
    # 'organizations': {
    #     'datasource': {
    #         'source': 'nodes',
    #         # 'projection': {**node_base_projection},
    #         'filter': {
    #             'category': {'$eq': 'organization'}
    #         }
    #     }
    # },

    # 'works': {
    #     'datasource': {
    #         'source': 'nodes',
    #         # 'projection': {**node_base_projection},
    #         'filter': {
    #             'category': {'$eq': 'work'}
    #         }
    #     }
    # },
    # 'edges': {
    #     'schema': {**edges.schema}
    # },
    # 'collections': {
    #     'schema': {**collections.schema}
    # },
    # 'users': {
    #     'schema': {**users.schema}
    # },
    # 'files': {
    #     'schema': {**files.schema}
    # },
    # 'locations': {
    #     'schema': {**locations.schema}
    # },
    # 'tags': {
    #     'schema': {**tags.schema}
    # },
    # 'pages': {
    #     'schema': {**pages.schema}
    # },
}
