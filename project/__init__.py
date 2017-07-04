from .app import app, graph

label_unique = {
    'Base': ['slug'],
    'Record': ['slug'],
    'Person': ['slug'],
}

for k, v in label_unique.items():
    for p in label_unique[k]:
        if p not in graph.schema.get_uniqueness_constraints(k):
            graph.schema.create_uniqueness_constraint(k, p)
