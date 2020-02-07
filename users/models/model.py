from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import app, db
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db = SQLAlchemy(app)

# print('sqlite:///' + os.path.join(basedir, 'data.sqlite'))


class Voter(db.Model):
    __tablename__ = 'voters'
    uuid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), index=True, unique=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    position_name = db.Column(db.Text)
	# username = db.Column(String(256))

    def __repr__(self):
        return 'Voter %r' % self.username
