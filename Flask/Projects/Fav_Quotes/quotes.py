from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# For database on local machine, using Valentina Studio, create database 'quote' for user 'postgres', replace <pwd> with password
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:<pwd>@localhost/quotes'

# For deployed app on Heroku, once the app is created (but before deployment) on Heroku, the Postgres database is provisioned via 'Resources' on Heroku
# Replace <username>, <pwd> and <server> from credentials in Heroku
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://<username>:<pwd>@<server>'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))

# For both local machine and Heroku-deployed versions:
# Now to create the table in the already created database 'quotes':
# Open Terminal (from within VSCode possible) and go to project directory .\Projects\Fav_Quotes
# Open Python (venv) .\Projects\Fav_Quotes>python
# >>> from quotes import db
# >>> db.create_all()
# >>> exit()



@app.route('/')
def index():
    result = Favquotes.query.all() # Fetches and stores all records from table 'favquotes' to the variable 'result'
    return render_template('index.html', result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index')) # 'index' refers to the view function index()