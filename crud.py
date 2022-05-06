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



def create_rating(user, score, favorite_place_id, user_id, comment):

    rating = Ratings(user=user, favorite_place_id = favorite_place_id,user_id = user_id, score=score, comment = comment)
    print('successfully added fav place')
    return rating





if __name__ == '__main__':
    from server import app
    connect_to_db(app, "users")