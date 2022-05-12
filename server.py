

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



@app.route('/login')
def login():
    """shows log in from """
    return render_template('login.html')



@app.route('/logout')
def logout():
    del session['email']

    return redirect('/')



@app.route('/authentication', methods = ['POST'])
def authentication():
    """gets the information from '/login' and makes sure this person is in the database"""
    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)

    if user:
        if password == user.password:
            session["first_name"] = user.fname
            session['email'] = user.email  #*this will be used later for log out button 
            return redirect('/homepage')

    flash("Incorrect password or email. Please try again")
    return redirect('/login')



@app.route('/homepage')
def homepage():

    return render_template('homepage.html')




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




@app.route('/results', methods = ["POST"])

def results():

    # del session['list']

    session['list'] = {}

    term = request.form['type']
    location = request.form['location']

    results = get_results(term, location)
    if 'businesses' not in results:
        flash("Invalid City Please Try Again")
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



@app.route('/results')
def results2():

    results = session['list']


    return render_template('results.html', results = results)



@app.route('/results/<id>')
def results_info(id):
    #* MAKE SURE SESSION KEEPS UPDATING)
    results = search_by_id(id)


    #* This is sending the days to the html for me to use (days)
    Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # print(results)

    return render_template('results_details.html', results = results, days = Days)



@app.route('/<id>/add_fav')
def add_fav(id):
    """this code will check in the place is already on the fav list and it is, its will add it to the middle table """
    results = search_by_id(id)

    # print(results)
    check_db_place = crud.search_by_ylpid(id)
    # print(check_db_place)

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

        crud.create_fav_place(place.place_id, user.user_id)
#!
    else:
        in_fav = crud.get_by_place_user(user.user_id, check_db_place.place_id)
        if in_fav != None:
            flash("Already added to favorites")
            return redirect ('/favorite_places')
        else:
            crud.create_fav_place(check_db_place.place_id, user.user_id)

    return redirect('/favorite_places')


@app.route('/favorite_places')
def fav_list():
    logged_in_email = session.get('email')#! need to remove the add to favorite if not logged in 
    user = crud.get_user_by_email(logged_in_email)
    favs = crud.get_fav_by_user(user.user_id)

    return render_template('favorites.html', favorites = favs)

# @app.route("/map-info.json")
# def map_info():
 
#     return jsonify()

@app.route('/maps', methods=['GET'])
def maps():

    lon = request.args.get('longitude')
    lat = request.args.get('latitude')

    return render_template('maps.html', lon = lon, lat = lat)


if __name__ == '__main__':
    connect_to_db(app, "users")
    app.run(debug=True, host="0.0.0.0")