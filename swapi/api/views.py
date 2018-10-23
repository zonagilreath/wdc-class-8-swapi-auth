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
from api.serializers import PeopleSerializer, PeopleModelSerializer, PlanetModelSerializer


class PeopleListApiView(APIView):

    def get(self, request):
        qs = People.objects.select_related('homeworld').all()
        serializer = PeopleSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            People.objects.create(
                name=serializer.validated_data['name'],
                homeworld=serializer.validated_data['homeworld'],
                height=serializer.validated_data['height'],
                mass=serializer.validated_data['mass'],
                hair_color=serializer.validated_data['hair_color'])
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class PeopleDetailApiView(APIView):

    def _get_object(self, people_id):
        return get_object_or_404(People, pk=people_id)

    def get(self, request, people_id):
        people = self._get_object(people_id)
        serializer = PeopleSerializer(people)
        return Response(serializer.data)

    def _update(self, request, people_id, partial=False):
        people = self._get_object(people_id)
        serializer = PeopleSerializer(data=request.data, partial=partial)
        if serializer.is_valid():
            for field in serializer.fields:
                if field in serializer.validated_data:
                    setattr(people, field, serializer.validated_data[field])
            people.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, people_id):
        return self._update(request, people_id, partial=False)

    def patch(self, request, people_id):
        return self._update(request, people_id, partial=True)

    def delete(self, request, people_id):
        people = self._get_object(people_id)
        people.delete()
        return Response(status=status.HTTP_200_OK)


class PeopleViewSet(viewsets.ViewSet):

    def _get_object(self, people_id):
        return get_object_or_404(People, pk=people_id)

    def list(self, request):
        qs = People.objects.select_related('homeworld').all()
        serializer = PeopleModelSerializer(qs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PeopleModelSerializer(data=request.data)
        if serializer.is_valid():
            People.objects.create(
                name=serializer.validated_data['name'],
                homeworld=serializer.validated_data['homeworld'],
                height=serializer.validated_data['height'],
                mass=serializer.validated_data['mass'],
                hair_color=serializer.validated_data['hair_color'])
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        people = self._get_object(pk)
        serializer = PeopleModelSerializer(people)
        return Response(serializer.data)

    def _update(self, request, people_id, partial=False):
        people = self._get_object(people_id)
        serializer = PeopleSerializer(data=request.data, partial=partial)
        if serializer.is_valid():
            for field in serializer.fields:
                if field in serializer.validated_data:
                    setattr(people, field, serializer.validated_data[field])
            people.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        return self._update(request, pk, partial=False)

    def partial_update(self, request, pk=None):
        return self._update(request, pk, partial=True)

    def destroy(self, request, pk=None):
        people = self._get_object(pk)
        people.delete()
        return Response(status=status.HTTP_200_OK)


class PeopleModelViewSet(viewsets.ModelViewSet):

    serializer_class = PeopleModelSerializer
    queryset = People.objects.all()


class PlanetModelViewSet(viewsets.ModelViewSet):

    serializer_class = PlanetModelSerializer
    queryset = Planet.objects.all()
