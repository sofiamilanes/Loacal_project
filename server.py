from crypt import methods
from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key = "shhh"

@app.route( '/')
def index():

    return render_template('base.html')

@app.route('/login', methods = ["POST"])
def login():

    return render_template('login.html')

@app.route('/homepage', methods = ["POST"])
def homepage():

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']

    return render_template('homepage.html',)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")