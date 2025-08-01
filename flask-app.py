# importing the Flask object from the flask module
# (that we installed with pip3 install flask)
import random as rn 
from flask import Flask, render_template


GREETINGS = ['Hello', "Good Day", "Good Night", "Welcome!"]

# instantiating the flask app 
app = Flask(__name__)

# register home route (/) to app
@app.route("/hello")
def hello_world():
    """ 
    return hello world to user 
    """
    return "<p>Hello, World!</p>"

@app.route('/')
def index():
    """
    load index.html
    """
    # looks in templates directory by default 
    return render_template('index.html')

@app.route('/about')
def about():
    """
    return about page to user
    """
    return "<p>About Me</p>"


# Exercise:
# add a route /greeting that randomly selects a greeting from the following list   
@app.route('/greeting')
def greeting():
    """
    Randonly select a greeting from the following list 
    """
    rand_idx = rn.randint(0, len(GREETINGS) - 1)
    greet_ = GREETINGS[rand_idx]
    return f"<h2> {greet_}</h2>"

# run app on port 5000, debug=True reruns the app on code changes
app.run(port=5000, debug=True)