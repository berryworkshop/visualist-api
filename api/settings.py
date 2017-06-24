class _BaseConfig:
    DEBUG = False
    TESTING = False
    GRAPH_DATABASE = 'http://localhost:7474/db/data/'
    GRAPH_USER = 'neo4j'
    GRAPH_PASSWORD = 'abcd1234'

    # TODO: Override this as a default when using Neo4j as a data layer
    ITEM_URL = 'regex("[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")'


class DevelopmentConfig(_BaseConfig):
    DEBUG = True
    TESTING = True


class TestingConfig(_BaseConfig):
    DEBUG = False
    TESTING = True


class ProductionConfig(_BaseConfig):
    pass
