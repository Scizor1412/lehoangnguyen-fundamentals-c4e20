from models.customer import Customer
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

for i in range (50):
    print ("Saving service", i+1, "....")
    new_customer = Customer(
        name = fake.name(),
        yob = randint(1990, 2000),
        gender = randint(0, 1),
        height = randint(150, 190),
        phone = fake.phone_number(),
        address = fake.address(),
        job = fake.job(),
        company = fake.company(),
        email = fake.email()
    )

    new_customer.save()