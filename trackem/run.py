from flask import Flask
from database.user import User
from database.session import session

app = Flask(__name__)

@app.route('/users')
def users():
	arr = []
	return ','.join(str(instance.__dict__) for instance in session.query(User).order_by(User.id))
	