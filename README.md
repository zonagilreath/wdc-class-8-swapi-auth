# SWAPI auth

We keep improving our SWAPI (https://swapi.co/) clone with more features. Now we will add some security layers on top of the REST API we built in our [previous project](https://github.com/rmotr-curriculum/wdc-class-6-swapi-drf). To do so, we will learn about two important topics to keep in mind while working with APIs: Authentication and Permissions.

## Authentication

Authentication will try to identify "who" is the person performing a request to our service. We will see that `rest-framework` supports most of the common authentication mechanisms out of the box. We can also write our own custom rules if we need.


* Basic Authentication (user & password)
    * `base64.b64encode("testing:RMOTR123".encode("utf-8"))`
    * `Authorization: Basic dGVzdGluZzpSTU9UUjEyMw==`
* Session Authentication
* Token Authentication
    * `Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`
* Custom rules (API client)
* JWT (https://github.com/GetBlimp/django-rest-framework-jwt)

## Permissions

Now that we know "who" the user is, we need to make sure she/he has the proper permissions to perform the action. To do so, `rest-framework` comes with a Permissions framework out of the box. We can either use a predefined set of permissions it provides:

* AllowAny
* IsAuthenticated
* IsAdminUser
* IsAuthenticatedOrReadOnly
* ...and more

Or we can write our own Permission subclasses with custom rules.

## Pagination

When handling big amount of documents in a JSON response, it's a good practice to return the information paginated. Instead of returning all the information at once in a single response, we will return it in chunks, according to certain settings. These strategies are already provided by `rest-framework`:

* PageNumberPagination
* LimitOffsetPagination
* CursorPagination

But, as always, we are free to write our own ones.
