from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('people', views.PeopleModelViewSet, base_name='people')
router.register('planets', views.PlanetModelViewSet, base_name='planets')

urlpatterns = []
urlpatterns += router.urls
