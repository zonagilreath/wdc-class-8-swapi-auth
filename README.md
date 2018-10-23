# SWAPI auth

```
basic auth (user, passwd)
    import base64
    base64.b64encode("testing:RMOTR123".encode("utf-8"))
    Authorization: Basic dGVzdGluZzpSTU9UUjEyMw==
session auth
token auth
    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
custom auth (api client)
JWT
```


## Permissions
```
AllowAny
IsAuthenticated
IsAdminUser
IsAuthenticatedOrReadOnly
```
