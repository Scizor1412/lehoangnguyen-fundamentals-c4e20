from models.service import Service
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()
characters_list = ['ngoan hiền', 'xinh xắn', 'đáng yêu', 'học giỏi']

for i in range (20):
    print ("Saving service", i+1, "....")
    new_service = Service(
        name = choice (['Tú Linh', 'Bảo Anh', "Đoan Trang", 'Hiền Thục', 'An Japan', 'Phương Ly', 'Ribi Sachi']),
        yob = randint(1990, 2000),
        gender = randint(0, 1),
        height = randint(150, 190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice ([True, False]),
        description = choice (characters_list),
        measurements = [90 +randint (-5, 5), 60 +randint (-5, 5), 90 +randint (-5, 5)]
    )

    new_service.save()