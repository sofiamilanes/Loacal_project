
import email
from flask import Flask, render_template, redirect, request, session, flash
from yelp_search import get_results
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "SECTRET KEY"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """returns registarion form"""

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
        print('cant')
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
    list_of_places = []
    term = request.form['type']
    location = request.form['location']

    results = get_results(term, location)
    for place in results['businesses']:
        list_of_places.append(place)

    return render_template('results.html', results = list_of_places)






if __name__ == '__main__':
    connect_to_db(app, "users")
    app.run(debug=True, host="0.0.0.0")