# Local Host 500
An app that allows you to search for locally owned palces in the area of your chosing.

## Summary




**Local Host 500** is seracheble tool that allows you to look up locally owned places near the area you have selecetd. It allwos you to get direcetion, save your favorites and comment on the palces you have been to. This is allwoing you to support small buissnes and keep the community growing
Back End: Python3, Flask framework, SQLAlchemy ORM, Postgresql database
Front End: JavaScript, AJAX, JSON, Jinja2, Bootstrap5, HTML, CSS, JQuery
APIs: Google Maps API && Yelp API

Features
Non-logged in users are able to look up buissness and get directions.


In order to save data and use more features that Local Host 500 has to offer, users might choose to sign up. If so, they are able to save the palces to be more easily accesable later on.


Users can also update their profile. Edit comments and favor and unfavor new palces.



## Local Installation
Requirements:
Need to acquire Google API key and don't forget to limit the key to only work on your browser, this key will need to be activated for both Google Maps.

Need to acquire Yelp API key.

Clone repository:

$ git clone https://github.com/sofiamilanes/Loacal_project.git
Setup Flask:
Create a virtual environment:

$ virtualenv env
Activate the virtual environment:

$ source env/bin/activate
Install dependencies:

$ pip3 install -r requirements.txt
Setup Credentials/Secrets:
Create a secrets.sh file

Setup the database:
Once your API credentials are retrieved, you can create and seed your database.

With PostgreSQL installed, create your database 'Users':

$ createdb Users
Create your database tables:

$ python3 model.py
Seed the database by using some modified data from Redfin and Bigger Pockets:

$ python3 seed.py
To start the Flask web server, run:

$ python3 server.py
In your browser, visit http://localhost:5000/

### Connect and learn more about Sofia on LinkedIn.
<a href="https://www.linkedin.com/in/sofia-milanes" target="_blank">Sofia's LinkedIn</a>
