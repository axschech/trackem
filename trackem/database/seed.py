import session
from user import User
import random
import os


class Seeder:
	def __init__(self):
		session.Base.metadata.create_all(session.engine)
		__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		self.names = open(os.path.join(__location__,'data/fakes.txt')).read().splitlines()

		self.generate_users();

	def getName(self):
		name = random.choice(self.names)
		self.names.remove(name)
		return name

	def generate_users(self):
		for x in range(10):
			session.session.add(User(first_name=self.getName(), last_name=self.getName(), email=self.getName() + '@test.com'))
		session.session.commit()

seeder = Seeder()