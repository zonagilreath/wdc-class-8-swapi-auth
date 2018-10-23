import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from api.models import People, Planet
from api.serializers import PeopleModelSerializer, PlanetModelSerializer


class PeopleModelViewSet(viewsets.ModelViewSet):

    serializer_class = PeopleModelSerializer
    queryset = People.objects.all()


class PlanetModelViewSet(viewsets.ModelViewSet):

    serializer_class = PlanetModelSerializer
    queryset = Planet.objects.all()
