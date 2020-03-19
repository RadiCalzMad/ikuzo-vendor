from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '0b735c2ab2e31jg456300a11f82dfc71'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ikuzo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

from ikuzoapp import routes