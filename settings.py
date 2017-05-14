class _BaseConfig:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(_BaseConfig):
    DEBUG = True
    TESTING = True


class TestingConfig(_BaseConfig):
    DEBUG = False
    TESTING = True


class ProductionConfig(_BaseConfig):
    pass
