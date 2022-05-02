from flask import Flask, render_template, redirect, session, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")