from flask import Flask

app = Flask(__name__)
app.secret_key = 'this is my secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dbuser:letmein00!@172.16.15.131/rrftc'

from models import db


db.init_app(app)


import rrftc.routes

