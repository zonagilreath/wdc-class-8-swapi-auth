from rest_framework import permissions


class IsUsernameStartingWithA(permissions.BasePermission):

    # view level permission
    def has_permission(self, request, view):
        return request.user and request.user.username.startswith('a')


class IsEvenPeopleID(permissions.BasePermission):

    # object level permission
    def has_object_permission(self, request, view, obj):
        if obj.id % 2 == 0:
            return True
        return False
