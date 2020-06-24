# from urllib import request
# from jose import jwt
# from social_core.backends.oauth import BaseOAuth2
# from urllib import request
# from jose import jwt
# from social_core.backends.oauth import BaseOAuth2
# from social_core.backends.auth0 import Auth0OAuth2


# class Auth0(BaseOAuth2):
#     """Auth0 OAuth authentication backend"""
#     name = 'auth0'
#     SCOPE_SEPARATOR = ' '
#     ACCESS_TOKEN_METHOD = 'POST'
#     REDIRECT_STATE = False
#     EXTRA_DATA = [
#         ('picture', 'picture'),
#         ('email', 'email')
#     ]

#     def authorization_url(self):
#         return 'https://' + self.setting('dev-405n1e6w.auth0.com') + '/authorize'

#     def access_token_url(self):
#         return 'https://' + self.setting('dev-405n1e6w.auth0.com') + '/oauth/token'

#     def get_user_id(self, details, response):
#         """Return current user id."""
#         return details['user_id']

#     def get_user_details(self, response):
#         # Obtain JWT and the keys to validate the signature
#         id_token = response.get('id_token')
#         jwks = request.urlopen(
#             'https://' + self.setting('dev-405n1e6w.auth0.com') + '/.well-known/jwks.json')
#         issuer = 'https://' + self.setting('dev-405n1e6w.auth0.com') + '/'
#         audience = self.setting('7ECrruuGVEjBOGcGyTqbRPvg4hQFXqRa')  # CLIENT_ID
#         payload = jwt.decode(id_token, jwks.read(), algorithms=['RS256'], audience=audience, issuer=issuer)

#         return {'username': payload['nickname'],
#                 'first_name': payload['name'],
#                 'picture': payload['picture'],
#                 'user_id': payload['sub'],
#                 'email': payload['email']}


# class Auth0(Auth0OAuth2):
#     def get_user_details(self, response):
#         # Obtain JWT and the keys to validate the signature
#         id_token = response.get('id_token')
#         jwks = request.urlopen('https://' + self.setting('DOMAIN') + '/.well-known/jwks.json')
#         issuer = 'https://' + self.setting('DOMAIN') + '/'
#         audience = self.setting('KEY')  # CLIENT_ID
#         payload = jwt.decode(id_token, jwks.read(), algorithms=['RS256'], audience=audience, issuer=issuer)

#         return {
#             'username': payload['nickname'],
#             'first_name': payload['name'],
#             'picture': payload['picture'],
#             'user_id': payload['sub'],
#             'role': payload['https://django-webapp/role'],
#         }
