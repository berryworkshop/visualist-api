from neomodel import StructuredNode, StringProperty, DateProperty, UniqueIdProperty

class Event(StructuredNode):
    slug = StringProperty(unique_index=True, blank=False)
    name = StringProperty(blank=False)
    description = StringProperty(blank=False)

