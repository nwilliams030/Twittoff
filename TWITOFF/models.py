from flask_sqlalchemy import sqlalchemy

# create a databases
DB = SQLAlchemy()

class User(DB.Model):
    """ one class for users, subclass"""
    # Two columns, (type of data,primary key)
    id = DB.Column(DB.BigInteger, primary_key = True )
    name = DB.Column(DB.String(15), nullable=False)

# one class for tweets
class Tweets(DB.Model):
    """ one class for users, subclass"""
    id = DB.Column(DB.BigInteger, primary_key = True)
    name = DB.Column(DB.Unicode(280))
