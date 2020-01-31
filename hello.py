""" Minimal flask app """
from flask import Flask, render_template

# pasting it in this way allows us to read in the name of the file
app = Flask(__name__)

# add a route - decorator, gets used to match URLs to particular funcitons in flask
@app.route('/')
# add hello function
def hello():
  return render_template('home.html')

# make a second route
@app.route("/about")
def preds():
    return render_template('about.html')
