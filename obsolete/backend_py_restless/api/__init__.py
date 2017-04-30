from .app import app
# from .models import graph

label_unique = {
    "User": ["id", "username"],
    "Tag": ["id", "name"],
    "Post": ["id"]
}

# for k, v in label_unique.items():
#     for p in label_unique[k]:
#         if p not in graph.schema.get_uniqueness_constraints(k):
#             graph.schema.create_uniqueness_constraint(k, p)
