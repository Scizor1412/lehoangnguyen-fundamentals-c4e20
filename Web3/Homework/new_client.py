import mlab
from faker import Faker
from random import choice, randint, sample
from Models.client import Client

mlab.connect()
fake = Faker()
characters_list = (['xinh đẹp', 'ngoan', 'hiền', 'học giỏi', 'thông minh', 'cao ráo', 'trắng trẻo', 'khôn khéo', 'khéo tay', 'biết nấu ăn'])

for i in range (20):
    characters = sample (characters_list, 3)
    err = randint (-5, 5)
    name = choice (['Tú Linh', 'Đoan Trang', 'Hiền Thục','Bảo Anh', 'An Japan', 'Ribi Sachi', 'Phương Ly'])
    print ('printing', i+1, "service")
    new_client = Client (
        name = name,
        yob = randint(1990, 2000),
        job = fake.job(),
        phone = fake.phone_number(),
        company = fake.company(),
        height = randint (160, 170),
        address = fake.address(),
        status = choice ([True, False]),
        description = characters,
        image = 'D:\Techkids\WebModule\Web3\Homework\Static\{}.jpg'.format(name),
        measurements = [90 + err, 60 + err, 90 + err]
    )

    new_client.save()