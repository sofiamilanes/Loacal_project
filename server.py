

from crypt import methods
from flask import Flask, jsonify, render_template, redirect, request, session, flash
from yelp_search import get_results, search_by_id
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import datetime

app = Flask(__name__)
app.secret_key = "SECTRET KEY"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """returns registarion form"""
    if 'email' in session:
        return redirect('/homepage')

    return render_template('register.html')

@app.route('/homepage')
def homepage():

    return render_template('homepage.html')



################################# login/logout

@app.route('/login')
def login():
    """shows log in from """
    return render_template('login.html')



@app.route('/logout')
def logout():
    del session['email']

    return redirect('/')


################################### registration/ authentication

@app.route('/registration', methods = ["POST"])
def registration():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email= request.form['email']
    password = request.form['password']


    if request.form['conf-password'] != password:
        flash("passwords did not match please try again")
        return redirect('/')

    user = crud.get_user_by_email(email)
    if user:
        flash("Email already exist, please try to log in")
        return redirect('/')

    else:
        crud.create_user(fname = first_name,
                lname = last_name,
                email= email,
                password=password )
        flash("Account created! Please log in")

    return redirect('/login')

@app.route('/authentication', methods = ['POST'])
def authentication():
    """gets the information from '/login' and makes sure this person is in the database"""
    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)

    if user:
        if password == user.password:
            session["first_name"] = user.fname.title()
            session['email'] = user.email  #*this will be used later for log out button 
            return redirect('/homepage')

    flash("Incorrect password or email. Please try again")
    return redirect('/login')




##################################### results


@app.route('/results')
def results2():

    results = session['list']


    return render_template('results.html', results = results)



@app.route('/results', methods = ["POST"])

def results():

    # del session['list']

    session['list'] = {}

    term = request.form['type']
    location = request.form['location']

    results = get_results(term, location)
    if 'businesses' not in results:
        flash("Invalid City, Please Try Again")
        return redirect('/homepage')
    else:
        for place in results['businesses']:
            session['list'][place['id']] = {}
            session['list'][place['id']]['name'] =[place][0]["name"]
            session['list'][place['id']]['id'] =[place][0]["id"]
            session['list'][place['id']]['city'] =[place][0]["location"]['city']
            session['list'][place['id']]['state'] =[place][0]["location"]['state']
            # session['list'][place['id']]['coordinates'] = [place][0]["coordinates"]#! DONT THINK I NEED THIS!


    return redirect('/results')



@app.route('/results/<id>')
def results_info(id):
    #* MAKE SURE SESSION KEEPS UPDATING)
    results = search_by_id(id)
    user = crud.get_user_by_email(session.get('email'))
    place_id = crud.get_placeId_byyelp(id)
    print(results)

    #? THIS IT TO CHECK IF THE PERSON ALREADY RATED THE PLACE
    if user != None:
        rated = crud.get_rating(user.user_id, place_id)
    else:
        rated = None

    if place_id != None:
        average = crud.avarage(place_id)

        # print("THIS IS THE AVARAGE", avarage)
        if average != None:

            average =  '{0:.2g}'.format(average)

        else:
            average = "No reviews yet"
    else:
        average = "No reviews yet"
    Hours = {}
    if "hours" not in results:
        return render_template('results_details.html', results = results,average=average, rated = rated, user = user)
    for item in results['hours'][0]['open']:
        if item['day'] in Hours:
                    Hours[item['day']]['end'] +=  datetime.datetime.strptime(item['end'],'%H%M').strftime(' %I:%M %p')
                    Hours[item['day']]['start']  += datetime.datetime.strptime(item['start'],'%H%M').strftime(' %I:%M %p') 
        else:
            Hours[item['day']] = {'end':datetime.datetime.strptime(item['end'],'%H%M').strftime(' %I:%M %p'),
                            'start':datetime.datetime.strptime(item['start'],'%H%M').strftime(' %I:%M %p') }

    #* This is sending the days to the html for me to use (days)
    Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    print(Hours)

    return render_template('results_details.html', results = results, days = Days, Hours = Hours, average=average, rated = rated, user = user)



##################################### ratings


#! unable to create rating unless place is in DB, which is only added if anyone adds to favorites
@app.route('/<id>/addRatings')
def add_ratings(id):
    id = id
    return render_template('rate.html', id = id)

@app.route('/<id>/editrating')
def editrating(id):
    id = id
    user = crud.get_user_by_email(session.get('email'))
    place_id = crud.get_placeId_byyelp(id)
    rated = crud.get_rating(user.user_id, place_id)


    return render_template('editRating.html', rated = rated, id = id)


@app.route('/<id>/editrating', methods = ['POST'])
def UpdateRating(id):
    check_db_place = crud.search_by_ylpid(id)
    user = crud.get_user_by_email(session.get('email'))
    score = request.form['rating']
    comment = request.form['comment']

    rating= crud.update_rating(user.user_id, check_db_place.place_id, score=score, comment=comment)
    return redirect(f'/{id}/viewRatings')



@app.route('/<id>/rating', methods = ['POST'])
def rating(id):
    score = request.form['rating']
    comment = request.form['comment']
    results = search_by_id(id)
    check_db_place = crud.search_by_ylpid(id)
    print(comment)

    logged_in_email = session.get('email')
    user = crud.get_user_by_email(logged_in_email)
    print("THIS IS THE USER", user.user_id)

    if check_db_place == None:

        place_ylp_id = results['id']
        name = results['name']
        city = results['location']['city']
        zip_code = results['location']['zip_code']
        address = results['location']['address1']
        place = crud.create_place(place_ylp_id = place_ylp_id, name=name, city=city, zip_code= zip_code, address=address)
        rating = crud.create_ratings(score= score, place_id=place.place_id, user_id=user.user_id,comment=comment)

    else:
        rating = crud.create_ratings(score= score, place_id=check_db_place.place_id, user_id=user.user_id, comment=comment)
    return redirect(f'/{id}/viewRatings')


@app.route('/<id>/viewRatings')
def view_ratings(id):
    id = id
    print("THIS IS THE ID",id)
    check_db_place = crud.search_by_ylpid(id)
    # print("THIS IS THE PLACE",check_db_place)
    if check_db_place != None:
        ratings = crud.get_all_ratings(check_db_place.place_id)
        # print(ratings)
        if ratings == []:
            flash("Currently Has No Reviews")
            return redirect(f'/results/{id}')

    else:
        flash("Currently Has No Reviews")
        return redirect(f'/results/{id}')


    return render_template('ratings.html', ratings = ratings, id = id)





##################################### favorites



@app.route('/<id>/add_fav')
def add_fav(id):
    """this code will check in the place is already on the fav list and it is, its will add it to the middle table """
    results = search_by_id(id)

    # print(results)
    check_db_place = crud.search_by_ylpid(id)
    # print(check_db_place.place_id)

    logged_in_email = session.get('email')#! need to remove the add to favorite if not logged in 
    user = crud.get_user_by_email(logged_in_email)

    if logged_in_email == None:
        flash(" You have to log in to add to favorites!")

    #* if the palce is not the db, it will add it to db and the middle table
    if check_db_place == None:

        place_ylp_id = results['id']
        name = results['name']
        city = results['location']['city']
        zip_code = results['location']['zip_code']
        address = results['location']['address1']
        place = crud.create_place(place_ylp_id = place_ylp_id, name=name, city=city, zip_code= zip_code, address=address)
        # print(place)
        # print(place.place_id)
        # check_db_place = crud.search_by_ylpid(id)

        fav_place = crud.create_fav_place(place.place_id, user.user_id)
        # print("THIS IS MY LIKES ",fav_place.likes)
#!
    else:
        in_fav = crud.get_by_place_user(user.user_id, check_db_place.place_id)
        if in_fav != None:
            if in_fav.likes == True:
                flash("Already added to favorites")
                return redirect ('/favorite_places')
            else:
                crud.change_to_like(user.user_id, check_db_place.place_id)
                return redirect ('/favorite_places')
        else:
            crud.create_fav_place(check_db_place.place_id, user.user_id)

    return redirect('/favorite_places')


@app.route('/<id>/unlike')
def unlike(id):
    check_db_place = crud.search_by_ylpid(id)
    logged_in_email = session.get('email')
    user = crud.get_user_by_email(logged_in_email)

    in_fav = crud.change_to_dislike(user.user_id, check_db_place.place_id)
    # print("EITHER TRUE OR FALSE", in_fav.likes)
    return "Success"
    # return redirect('/favorite_places')


@app.route('/favorite_places')
def fav_list():
    logged_in_email = session.get('email')
    user = crud.get_user_by_email(logged_in_email)
    favs = crud.get_fav_by_user(user.user_id)
    # print(favs.likes)

    return render_template('favorites.html', favorites = favs)



######################################## maps

@app.route('/maps', methods=['GET'])
def maps():

    lon = request.args.get('longitude')
    lat = request.args.get('latitude')

    return render_template('maps.html', lon = lon, lat = lat)




##########################################

if __name__ == '__main__':
    connect_to_db(app, "users")
    app.run(debug=True, host="0.0.0.0")