from neo4j.v1 import GraphDatabase, basic_auth

# create, read, update, destroy
#     person
#     organization
#     work
#     event

class DatabaseConnection(object):

    def __init__(self):
        driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "wormh0Le"))
        self.session = driver.session()

        # result = session.run("MATCH (a:Person) WHERE a.name = {name} "
        #     "RETURN a.name AS name, a.title AS title",
        #     {"name": "Arthur"})

        # for record in result:
        #     print("%s %s" % (record["title"], record["name"]))
        #     session.close()


    def create(node_type, properties):
        self.session.run(
            "CREATE (a:Person {name: {name}, title: {title}})",
            {"name": "Arthur", "title": "King"}
        )
        return node

    def read(node_id):
        node = None
        return node

    def update(node_id, properties):
        node = None
        return node

    def destroy(node):
        return true

    def connect_nodes(subject_node_id, predicate, object_node_id):
        return true
