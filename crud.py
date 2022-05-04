from model import db, User, Places, Ratings, User_fav_places, Type_of_place, connect_to_db

def create_user(fname, lname, email, password):

    user = User(fname = fname, lname = lname, email = email, password = password)
    print('sucessfulyy added ')
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()

    
def create_place(name, city, zip_code, address):

    place = Places(name = name, city = city, zip_code = zip_code, address = address)

    return place



def create_fav_place(favorite_place_id, user_id):

    fav_place = User_fav_places(favorite_place_id = favorite_place_id,user_id = user_id)

    return fav_place



def create_rating(user, score, favorite_place_id, user_id, comment):

    rating = Ratings(user=user, favorite_place_id = favorite_place_id,user_id = user_id, score=score, comment = comment)

    return rating





if __name__ == '__main__':
    from server import app
    connect_to_db(app, "users")