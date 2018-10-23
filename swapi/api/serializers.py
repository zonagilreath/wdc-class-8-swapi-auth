from rest_framework import serializers

from api.models import People, Planet


class PeopleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('id', 'name', 'homeworld', 'height', 'mass', 'hair_color', 'created')


class PlanetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ('id', 'name', 'population', 'diameter')
