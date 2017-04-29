from neomodel import StructuredNode, StringProperty, DateProperty, UniqueIdProperty


class Book(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(unique_index=True)
    content = StringProperty(default='', blank=True)
    published = DateProperty()
