import os
import json

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from api.models import Planet, People


def get_obj_from_url(Model, url):
    obj_id = int(url.strip('/').split('/')[-1])
    return Model.objects.get(id=obj_id)


class Command(BaseCommand):
    help = 'Cleans all objects in the DB and imports data from JSON files.'

    def handle(self, *args, **options):
        # import planets
        Planet.objects.all().delete()
        with open(os.path.join(settings.BASE_DIR, 'api/data/planets.json')) as f:
            planets = json.load(f)
        for index, doc in enumerate(planets, 1):
            try:
                population = int(doc['population'])
            except ValueError:
                population = None
            try:
                diameter = int(doc['diameter'])
            except ValueError:
                diameter = None
            Planet.objects.create(
                id=index,
                name=doc['name'],
                population=population,
                diameter=diameter,
            )

        # import people
        People.objects.all().delete()
        with open(os.path.join(settings.BASE_DIR, 'api/data/people.json')) as f:
            people = json.load(f)
        for index, doc in enumerate(people, 1):
            homeworld = get_obj_from_url(Planet, doc['homeworld'])
            try:
                height = int(doc['height'])
            except ValueError:
                height = None
            try:
                mass = int(doc['mass'])
            except ValueError:
                mass = None
            People.objects.create(
                id=index,
                name=doc['name'],
                homeworld=homeworld,
                height=height,
                mass=mass,
                hair_color=doc['hair_color'],
            )
