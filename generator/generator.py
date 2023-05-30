import random

from data.data import Person
from faker import Faker


def generate_person():
    return Person(
        first_name= Faker('en').first_name(),
        last_name= Faker('en').last_name(),
        email= Faker('en').email(),
        subject= 'English',
        number= Faker('en').msisdn(),
        address= Faker('en').street_address() + ', ' + Faker('en').building_number(),
        permanentAddress= Faker('en').street_address() + ', ' + Faker('en').building_number()

    )


def generate_file():
    path = rf'C:\Users\alisa\PycharmProjects\DEMOQA\test{random.randint(10, 100)}.txt'
    file = open(path, 'w')
    file.write('Гамарджоба')
    file.close()
    return path
