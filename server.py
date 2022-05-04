
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

@app.route('/authentication', methods = ['POST'])
def authentication():
    """gets the information from log in and makes sure this person is in session"""
    email = request.form['email']
    password = request.form['password']
    print(password)
    print(session['password'])

    if email != session['email']: #! need to change this to check on the db not session
        flash("Incorrect password or email. Please try again")
        return redirect('/login')
    if password != session['password']:#! need to change this to check on the db not session
        flash("Incorrect password or email. Please try again")
        return redirect('/login')
    return redirect('/homepage')


@app.route('/homepage')
def homepage():

 return render_template('homepage.html')

@app.route('/registration', methods = ["POST"])
def registration():

    if request.form['conf-password'] != request.form['password']:
        flash("passwords did not match please try again")
        return redirect('/')
    else:
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        session['password'] = request.form['password']

        crud.create_user(fname = session['first_name'], lname = session['last_name'], email=session['email'], password=session['password'] )


    return redirect('/homepage')


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