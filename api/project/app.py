import os, sys
from flask import Flask, jsonify
from py2neo import authenticate, Graph, Relationship

app = Flask(__name__)

app.config['NEO4J_USER']     = os.getenv('NEO4J_USER', 'neo4j')
app.config['NEO4J_PASSWORD'] = os.getenv('NEO4J_PASSWORD')

graph = Graph(
    host='neo4j',
    user=app.config['NEO4J_USER'],
    password=app.config['NEO4J_PASSWORD']
)

@app.route('/')
def hello_world():
    return jsonify({
        'Hello': 'world!'
    })

@app.route('/db')
def hello_db():
    return jsonify(graph.data("MATCH (a) RETURN a"))

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "message": "resource not found"
    }), 404

@app.errorhandler(500)
def page_not_found(e):
    return jsonify({
        "message": "server error"
    }), 500



# def configure_app(app):
#     config = {
#         "development": DevelopmentConfig,
#         "testing": TestingConfig,
#         "default": ProductionConfig,
#     }
#     config_name = os.getenv('FLASK_CONFIGURATION', 'default')
#     app.config.from_object(config[config_name])
