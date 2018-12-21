import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'credit_management.settings')

from random import choice
from string import ascii_letters, digits
import django
django.setup()
from faker import Faker
from basicfunc.models import Participant

fake = Faker()

def addUser(n = 10):
	for i in range(n):
		user_url = "".join(choice(ascii_letters + digits) for i in range(10))
		u = Participant.objects.get_or_create(name=fake.name(), email=fake.email(), credit_points=choice(range(1000)), link=user_url)[0]
		u.save()

def changeLinks():
	k = Links.objects.all()

	if k:
		for i in k:
			i.link = "".join(choice(ascii_letters + digits) for i in range(10))
			i.save(update_fields=["link"])

		
if __name__ == "__main__":
	print("Changing Links")
	addUser()
	print("Database Populated!")
