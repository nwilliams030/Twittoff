""" Write a fun web application for comparing and predicting tweets"""
from flask import Flask

# pasting it in this way allows us to read in the name of the file
app = Flask(__name__)

# add a route - decorator, gets used to match URLs to particular funcitons in flask
@app.route('/')
# add hello function
def hello():
  return("Hello World!")
