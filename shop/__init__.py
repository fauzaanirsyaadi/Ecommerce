from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/ecommerce' 
#postgresql(server data base)://postgres (username):admin (user password) @localhost:5432(port local server)/ecommerce (database name)'
db = SQLAlchemy(app)