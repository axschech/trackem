from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import session

class Business(session.Base):
	__tablename__ = 'buisnesses'

	id = Column(Integer, primary_key=True)
	name = Column(String(80), unique=True, nullable=False)
	email = Column(String(120), unique=True, nullable=False)

	users = relationship('User', secondary='buisness_users', back_populates='users')