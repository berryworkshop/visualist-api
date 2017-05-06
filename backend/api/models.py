from neomodel import (
    ArrayProperty,
    BooleanProperty,
    DateTimeProperty,
    FloatProperty,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
    RelationshipTo,
)
import pytz


class Base(StructuredNode):
    slug = StringProperty(unique_index=True, required=True)
    description = StringProperty(required=True)

    def date(self):
        pass

    def url(self):
        pass


class Record(Base):
    name = StringProperty(required=True)
    featured = BooleanProperty(default=False)
    approved = BooleanProperty(default=False)
    web_public = BooleanProperty(default=True)

    license = StringProperty(
        default="https://creativecommons.org/licenses/by-sa/4.0/")

    same_as = ArrayProperty() # urls
    categories = ArrayProperty(required=True) # strings, from controlled vocabularies

    # has_citation = RelationshipTo(Work)
    # has_source = RelationshipTo(Work)
    # has_tag = RelationshipTo(Tag)
    # licensed_by = RelationshipTo(Record)
    is_next_iteration_of = RelationshipTo('Record', 'IS_NEXT_ITERATION_OF')

    def citation(self):
        pass

    def date(self):
        pass


class Event(Record):
    __label__ = 'Record:Event'

    CATEGORIES = (
      ('course', 'course'),
      ('exhibition', 'exhibition'),
      ('performance', 'performance'),
      ('reception', 'reception'),
      ('residency', 'residency'),
      ('workshop', 'workshop'),
    )
    STATUSES = (
      ('active', 'active'),
      ('cancelled', 'cancelled'),
    )

    categories = ArrayProperty(required=True, choices=CATEGORIES)
    price_min = FloatProperty()
    price_max = FloatProperty()
    date_start = DateTimeProperty(default=lambda: datetime.now(pytz.utc))
    date_end = DateTimeProperty(default=lambda: datetime.now(pytz.utc))
    status = StringProperty(choices=STATUSES, default='active')
    group_friendly = BooleanProperty(default=True)

    # has_venue = RelationshipTo(Place, 'HAS_VENUE')
    # organized_by = RelationshipTo(Record, 'ORGANIZED_BY') # Person/Organization
    # curated_by = RelationshipTo(Record, 'CURATED_BY') # Person/Organization
    # produced_by = RelationshipTo(Record, 'PRODUCED_BY') # Person/Organization
    # contributed_by = RelationshipTo(Record, 'CONTRIBUTED_BY') # Person/Organization
    part_of = RelationshipTo('Event', 'PART_OF')

    def date(self):
        pass

    def duration(self):
        pass

    def distance(self):
        pass
