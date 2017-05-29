from passlib.apps import custom_app_context as pwd_context

from neomodel import StructuredNode, StringProperty, DateProperty, UniqueIdProperty


class User(StructuredNode):
    uid = UniqueIdProperty()
    username = StringProperty(unique_index=True, blank=False)
    passhash = StringProperty(blank=False)

    def __init__(username, password):
        super().__init__()
        self.username = username
        self.passhash = self.hash_password(password)

    def hash_password(self, password):
        self.passhash = pwd_context.encrypt(password)

    def authenticate(self, password):
        return pwd_context.verify(password, self.passhash)


class Book(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True)
    content = StringProperty(default='', blank=True)
    published = DateProperty()

