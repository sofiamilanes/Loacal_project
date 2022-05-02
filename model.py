from email.policy import default
from xmlrpc.client import boolean
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    #backref to ratings

class Fav_places(db.Model):
    __tablename__ = "fav_places"

    place_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)

    #backref to ratings

class Ratings(db.Model):

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Integer, nullable=False)
    favorite_place_id = db.Column(db.Integer, db.ForeignKey("fav_places.place_id"), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.user_id"), nullable=False)
    comment = db.Column(db.Text, nullable=True)
   

    place = db.relationship("Fav_places", backref="ratings")
    user = db.relationship("User", backref="ratings")

class User_fav_places(db.Model):

    __tablename__ = "user_fav_places"

    favorite_place_id = db.Column(db.Integer, db.ForeignKey("fav_places.place_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    likes = db.Column(db.boolean, default = True, nullable = False) #*make sure this is how you write it

class Type_of_place(db.Model):

    __tablename__ = "type_of_place"

    type = db.Column(db.String(70), nullable=False)
    favorite_place_id = db.Column(db.Integer, db.ForeignKey("fav_places.place_id"), nullable=False)
    
