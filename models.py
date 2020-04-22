import os
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

# database_name = "castency"
# database_path = "postgres://{}/{}".format('localhost:5432', database_name)
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

'''
Actor
Have name, age and gender
'''
class Actor(db.Model):  
    __tablename__ = 'Actor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    birthday = Column(DateTime)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'gender': self.gender }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

'''
Movie
Have title, and release date
'''
class Movie(db.Model):  
    __tablename__ = 'Movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime, nullable = False)


    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'release_date': self.release_date }
	
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

