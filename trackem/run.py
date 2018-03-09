from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/users')
def users():
	print database
	return ''