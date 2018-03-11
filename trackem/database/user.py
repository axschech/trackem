from sqlalchemy import Column, Integer, String
import session

class User(session.Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	first_name = Column(String(80), unique=False, nullable=False)
	last_name = Column(String(80), unique=True, nullable=False)
	email = Column(String(120), unique=True, nullable=False)