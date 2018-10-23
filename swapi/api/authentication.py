from rest_framework import exceptions
from rest_framework import permissions
from rest_framework import authentication

from django.core.exceptions import ValidationError

from api.models import APIClient


def validate_authkey(value):
    """Raises a ValidationError if value has not length 32"""
    if not len(value) == 32:
        raise ValidationError(
            'Value must be a string containing 32 alphanumeric characters')


class APIClientAuthentication(authentication.BaseAuthentication):
    """
    To create a custom authentication mechanism, you just need to override
    the `authenticate` method of `BaseAuthentication` class.

    Reference:
    https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
    """
    def authenticate(self, request):
        access_key = request.query_params.get('accesskey')
        if not access_key:
            return None

        try:
            validate_authkey(access_key)
        except ValidationError:
            raise exceptions.AuthenticationFailed('Invalid Accesskey')
        try:
            api_client = APIClient.objects.get(accesskey=access_key)
            if api_client.is_active:
                return (api_client, None)
            else:
                raise api_client.DoesNotExist
        except APIClient.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid Accesskey')
