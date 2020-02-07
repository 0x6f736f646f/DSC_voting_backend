from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView
from schemas.schemas import our_schema
from models.model import db, app

basedir = os.path.abspath(os.path.dirname(__file__))

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=our_schema, graphiql=True))

@app.route('/')
def index():
    return "GraphQL server is listening on /graphql"

if __name__ == "__main__":
    app.run()

