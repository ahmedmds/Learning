from flask import Flask, render_template

app = Flask(__name__) #__name__ is the module/package which is containing the application

@app.route('/') # '/' is the root URL, therefore just '/' could be homepage and e.g. '/contact' could be the Contact page which is an endpoint
def index(): # View function, contains the reponse to the request received by the application
    cities = ['Frankfurt', 'New York', 'Sydney']
    return render_template('index.html', cities=cities)


# Dynamic route
@app.route('/user/<name_endpoint>')
def user(name_endpoint):
    return render_template('user.html', name=name_endpoint)