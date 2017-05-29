from py2neo import Node


class BaseNode(Node):

    def __init__(self, *labels, **properties):
        super().__init__(*labels, **properties)

    @property
    def date(self):
        pass

    @property
    def url(self):
        pass

    @property
    def json(self):
        pass


class RecordNode(BaseNode):

    def __init__(self, *labels, **properties):
        super().__init__(*labels, **properties)


    @property
    def citation(self):
        pass

    @property
    def date(self):
        pass


class EventNode(RecordNode):

    def __init__(self, *labels, **properties):
        super().__init__(*labels, **properties)


    @property
    def date(self):
        pass

    @property
    def duration(self):
        pass

    @property
    def distance(self):
        pass
