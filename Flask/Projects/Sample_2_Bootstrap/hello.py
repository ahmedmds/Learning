from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__) #__name__ is the module/package which is containing the application

bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/') # '/' is the root URL, therefore just '/' could be homepage and e.g. '/contact' could be the Contact page which is an endpoint
def index(): # View function, contains the reponse to the request received by the application
    return render_template('index.html')


# Dynamic route
@app.route('/user/<name_endpoint>')
def user(name_endpoint):
    return render_template('user.html', name=name_endpoint)