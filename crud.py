from tkinter import Place
from model import db, User, Places, Ratings, User_fav_places, Type_of_place, connect_to_db
from sqlalchemy.sql import func


########################################### Users

def create_user(fname, lname, email, password):
    user = User(fname = fname, lname = lname, email = email, password = password)
    print('successfully added')
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()


def update_info(user_id, fname, lname, email):
    user = db.session.query(User).filter(User.user_id == user_id).first()
    user.fname = fname
    user.lname = lname
    user.email = email

    db.session.commit()
    return user

def update_pass(user_id, new_pass):
    user = db.session.query(User).filter(User.user_id == user_id).first()
    
    user.password = new_pass
    db.session.commit()

    return user


############################################ Places

def create_place(place_ylp_id, name, city, zip_code, address):

    place = Places(place_ylp_id = place_ylp_id,name = name, city = city, zip_code = zip_code, address = address)
    print('successfully added')
    db.session.add(place)
    db.session.commit()

    return place
def search_by_ylpid(id): 

    return Places.query.filter(Places.place_ylp_id == id).first()



def create_fav_place(favorite_place_id, user_id):
    fav_place = User_fav_places(favorite_place_id = favorite_place_id,user_id = user_id)
    print('successfully added place')
    db.session.add(fav_place)
    db.session.commit()
    return fav_place

def get_placeId_byyelp(ylp_id):
    id = db.session.query(Places.place_id).filter(Places.place_ylp_id == ylp_id).first()
    if id != None:
        return id[0]
    else:
        return id



############################################### Ratings

def create_ratings(score, place_id, user_id, comment ):
    rating = Ratings(score = score, favorite_place_id = place_id, user_id =user_id, comment = comment)
    print('Successfully added place')
    db.session.add(rating)
    db.session.commit()

    return rating

def avarage(place_id):
    ratings = db.session.query(func.avg(Ratings.score)).filter(Ratings.favorite_place_id == place_id).all()
    return ratings[0][0]


def view_ratings(place_id):

    ratings = db.session.query(Ratings).filter(Ratings.favorite_place_id == place_id).all()
    return ratings


def get_all_ratings(place_id):
    all_ratings = db.session.query(User.fname, User.lname, Ratings.score, Places.name, Ratings.comment).join(Places).filter(Ratings.favorite_place_id == place_id).join(User).filter(Ratings.user_id == User.user_id).all()
    return all_ratings


def get_rating(user, place):
    rating = db.session.query(Ratings).filter(Ratings.user_id == user,Ratings.favorite_place_id == place).first()
    return rating


def get_ratings_by_user(user):


    rating = db.session.query(Places.name, Places.place_ylp_id, Ratings.score, Ratings.comment,Ratings.created_at,Ratings.last_updated, User.fname, User.lname).join(User).filter(Ratings.user_id == user).join(Places).filter(Ratings.favorite_place_id == Places.place_id).order_by(Ratings.last_updated.desc()).all()
    for rate in rating:
        print(rate.created_at.hour, rate.last_updated)
    return rating

    # rating = db.session.query(Ratings).filter(Ratings.user_id == user).all()
    # return rating


def update_rating(user, place, score, comment):
    rating = db.session.query(Ratings).filter(Ratings.user_id == user,Ratings.favorite_place_id == place).first()
    rating.score = score
    rating.comment = comment
    db.session.commit()
    return rating


###################################################### Favorites

def get_fav_by_user(user):
    fav = db.session.query(Places.name, Places.place_ylp_id, Places.city, User_fav_places.likes,User_fav_places.created_at,User_fav_places.last_updated ).join(User_fav_places).filter(User_fav_places.favorite_place_id == Places.place_id).join(User).filter(user == User_fav_places.user_id).order_by(User_fav_places.last_updated.desc()).all()

    return fav

def get_by_place_user(user, place):
    fav_id = db.session.query(User_fav_places).filter(User_fav_places.user_id == user,User_fav_places.favorite_place_id == place).first()

    return fav_id

def change_to_dislike(user, place):
    fav_id = db.session.query(User_fav_places).filter(User_fav_places.user_id == user,User_fav_places.favorite_place_id == place).first()
    fav_id.likes = False
    db.session.commit()
    return fav_id

def change_to_like(user, place):
    fav_id = db.session.query(User_fav_places).filter(User_fav_places.user_id == user,User_fav_places.favorite_place_id == place).first()
    fav_id.likes = True
    db.session.commit()
    return fav_id

#! Not sure if I want to have a remove button just yet~!
# def delete_rating(user,place):
#     fav_id = db.session.query(Ratings).filter(Ratings.user_id == user, Ratings.favorite_place_id == place).first()
#     db.session.delete(fav_id)
#     db.session.commit()
#     return fav_id

#!




if __name__ == '__main__':
    from server import app
    connect_to_db(app, "users")