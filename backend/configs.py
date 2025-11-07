from flask import Flask # web framework
from flask_sqlalchemy import SQLAlchemy # database
from flask_cors import CORS # send requests from frontend to backend

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)