# from email.policy import default
# from xmlrpc.client import boolean
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique = True)
    password = db.Column(db.String(255), nullable=False)

    rating = db.relationship("Ratings", back_populates="user") #!user or users 
    fav_place = db.relationship("User_fav_places", back_populates="user")

class Places(db.Model):
    __tablename__ = "places"

    place_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)

    rating = db.relationship("Ratings", back_populates="place") #! places or place
    fav_place = db.relationship("User_fav_places", back_populates="place")

class Ratings(db.Model):

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Integer, nullable=False)
    favorite_place_id = db.Column(db.Integer, db.ForeignKey("places.place_id"), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.user_id"), nullable=False)
    comment = db.Column(db.Text, nullable=True)
   

    place = db.relationship("Places", back_populates="rating")
    user = db.relationship("User", back_populates="rating")

class User_fav_places(db.Model):

    __tablename__ = "user_fav_places"

    fav_places_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    favorite_place_id = db.Column(db.Integer, db.ForeignKey("places.place_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    likes = db.Column(db.Boolean, default = True, nullable = False) #*make sure this is how you write it

    place = db.relationship("Places", back_populates="fav_place") #!
    user = db.relationship("User", back_populates="fav_place") #!


class Type_of_place(db.Model):

    __tablename__ = "type_of_place"

    type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(70), nullable=False)
    favorite_place_id = db.Column(db.Integer, db.ForeignKey("places.place_id"), nullable=False)
    

if __name__ == "__main__":
    from server import app

    connect_to_db(app, 'users') #"users" changed after creating crud.py