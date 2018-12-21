import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import *
from rest_framework.permissions import *

from api.models import People, Planet
from api.serializers import PeopleModelSerializer, PlanetModelSerializer
from api.permissions import IsUsernameStartingWithA, IsEvenPeopleID
from api.pagination import TinyResultsPagination


class PeopleModelViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleModelSerializer
    queryset = People.objects.all()

    @action(detail=False, methods=['get'], url_path='custom-list-action')
    def custom_list_action(self, request, pk=None):
        return Response({
            'message': 'This is a custom List action'
        })

    @action(detail=True, methods=['get'], url_path='custom-detail-action')
    def custom_detail_action(self, request, pk=None):
        return Response({
            'message': "This is a custom Detail action for object '{}'".format(pk)
        })


class PlanetModelViewSet(viewsets.ModelViewSet):

    serializer_class = PlanetModelSerializer
    queryset = Planet.objects.all()
