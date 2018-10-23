from django.contrib import admin

from api.models import APIClient, People, Planet



@admin.register(APIClient)
class APIClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'accesskey', 'is_active')


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass
