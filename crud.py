from tkinter import Place
from model import db, User, Places, Ratings, User_fav_places, Type_of_place, connect_to_db

def create_user(fname, lname, email, password):

    user = User(fname = fname, lname = lname, email = email, password = password)
    print('successfully added')
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()
    

def create_place(place_ylp_id, name, city, zip_code, address):

    place = Places(place_ylp_id = place_ylp_id,name = name, city = city, zip_code = zip_code, address = address)
    print('successfully added')
    db.session.add(place)
    db.session.commit()

    return place
def search_by_ylpid(id): #!NEEEDDD TO FINISH THIS


    return Places.query.filter(Places.place_ylp_id == id).first()


def create_fav_place(favorite_place_id, user_id):



    fav_place = User_fav_places(favorite_place_id = favorite_place_id,user_id = user_id)
    print('successfully added place')
    db.session.add(fav_place)
    db.session.commit()
    return fav_place


def get_fav_by_user(user):
    # SELECT users.fname, places.name  FROM users JOIN user_fav_places ON users.user_id = user_fav_places.user_id JOIN places ON places.place_id = user_fav_places.favorite_place_id 
# WHERE user_fav_places.user_id = 2 AND user_fav_places.favorite_place_id = places.place_id


# SELECT  places.name  FROM users JOIN user_fav_places ON users.user_id = user_fav_places.user_id JOIN places ON places.place_id = user_fav_places.favorite_place_id 
# WHERE user_fav_places.user_id = 2 AND user_fav_places.favorite_place_id = places.place_id
# users-# GROUP BY places.name
# users-# ;

    # fav = db.session.query(User).join(User_fav_places).filter(User_fav_places.user_id == user).join(Places).filter(User_fav_places.favorite_place_id == Places.place_id).all()
    # fav = db.session.query(Places.name).join(User_fav_places).filter(User_fav_places.favorite_place_id == Places.place_id).join(User).filter(User.user_id == User_fav_places.user_id).all()
    fav = db.session.query(Places.name, Places.place_ylp_id).join(User_fav_places).filter(User_fav_places.favorite_place_id == Places.place_id).join(User).filter(user == User_fav_places.user_id).all()

    return fav

def get_by_place_user(user, place):
    fav_id = db.session.query(User_fav_places).filter(User_fav_places.user_id == user,User_fav_places.favorite_place_id == place).first()

    return fav_id


def create_rating(user, score, favorite_place_id, user_id, comment):

    rating = Ratings(user=user, favorite_place_id = favorite_place_id,user_id = user_id, score=score, comment = comment)
    print('successfully added fav place')
    return rating





if __name__ == '__main__':
    from server import app
    connect_to_db(app, "users")