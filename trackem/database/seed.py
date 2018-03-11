import session
from user import User
import random


class Seeder:
	def __init__(self):
		print session
		session.Base.metadata.create_all(session.engine)
		self.generate_users();

	def generate_users(self):
		for x in range(10):
			session.session.add(User(first_name=str(random.randint(1000,500000)), last_name=str(random.randint(1000,500000)), email=str(random.randint(1000,500000))))
		session.session.commit()

seeder = Seeder()