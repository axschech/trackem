from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import random

engine = create_engine('sqlite:///test.db', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	first_name = Column(String(80), unique=False, nullable=False)
	last_name = Column(String(80), unique=True, nullable=False)
	email = Column(String(120), unique=True, nullable=False)

class Seeder:
	session = Session()

	def __init__(self):
		Base.metadata.create_all(engine)
		self.generate_users();

	def generate_users(self):
		for x in range(10):
			self.session.add(User(first_name=str(random.randint(1000,500000)), last_name=str(random.randint(1000,500000)), email=str(random.randint(1000,500000))))
		self.session.commit()

seeder = Seeder()