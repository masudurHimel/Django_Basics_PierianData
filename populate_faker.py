import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoExcercise.settings')

import django

django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()


def populate(N=5):

    for i in range(N):
        top = fakegen.name()
        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        topic = Topic.objects.get_or_create(top_name=top)[0]
        webpg = Webpage.objects.get_or_create(topic=topic, name=fake_name, url=fake_url)[0]
        accRecord = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)


if __name__ == '__main__':
    print('Population start')
    populate(4)
    print("Population Done !! ")
