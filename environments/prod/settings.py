import os
from environ import Env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QUANTUMMANAGEMENT_BASE_HOSTNAME = ''

env = Env()


# Will always be there.
# - Locally will (should) have it.
# - Within docker container: copying from the /environments directory to root directory.
env.read_env(env_file=os.path.join(BASE_DIR, '.env'))

ENVIRONMENT = env.get_value("ENVIRONMENT")

# if ENVIRONMENT == "staging":
#   env.read_env(env_file=os.path.join(BASE_DIR, '/environments/stg/.env'))
# elif ENVIRONMENT == "production":
#   env.read_env(env_file=os.path.join(BASE_DIR, '/environments/prod/.env'))
# else:
#   env.read_env(env_file=os.path.join(BASE_DIR, '/environments/dev/.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_value("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env.get_value("DEBUG")

if ENVIRONMENT == "staging":
    ALLOWED_HOSTS = ['*']
elif ENVIRONMENT == "production":
    ALLOWED_HOSTS = [
        'http://127.0.0.1:8000/complete/auth0',
        'http://localhost:8000/complete/auth0',
        'http://localhost:8000/social-auth/complete/auth0',
        'https://api.quantumcoasters.com',
        'https://dev-405n1e6w.auth0.com/api/v2/',
        'https://dev-405n1e6w.auth0.com',
        'https://{QUANTUMMANAGEMENT_BASE_HOSTNAME}',
    ]
else:
  ALLOWED_HOSTS = ['localhost', '8000', '127.0.0.1', 'https://dev-405n1e6w.auth0.com', 'https://{QUANTUMMANAGEMENT_BASE_HOSTNAME}']



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'safedelete',
    'datetimepicker',
    'django_filters',
    'social_django',
    'quantummanagementapp',
    'django.contrib.sessions.middleware',
    ]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'quantummanagement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'quantummanagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# # If the flag as been set, configure to use proxy
# if env.get_value("USE_CLOUD_SQL_AUTH_PROXY", None):
#     DATABASES["default"]["HOST"] = "127.0.0.1"
#     DATABASES["default"]["PORT"] = 5432


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'TEST': {
        #     'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
        # }
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.get_value("PG_SQL_DATABASE"),
        'USER': env.get_value("PG_SQL_USER"),
        'PASSWORD': env.get_value("PG_SQL_PASSWORD"),
        'HOST': env.get_value("PG_SQL_HOST"),
        'PORT': env.get_value("PG_SQL_PORT"),
    },
   'cloudsql' : {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': env.get_value('CLOUD_SQL_DATABASE_NAME'),
       'USER': env.get_value('CLOUD_SQL_USERNAME'),
       'PASSWORD': env.get_value('CLOUD_SQL_PASSWORD'),
       'HOST': env.get_value('CLOUD_SQL_HOST'),
       # 'PORT': 5432,
       }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


if ENVIRONMENT == "staging":
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:8000',
        'http://127.0.0.1:8000',
    )
elif ENVIRONMENT == "production":
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:8000',
        'http://127.0.0.1:8000',
        "https://dev-405n1e6w.auth0.com",
        'https://{QUANTUMMANAGEMENT_BASE_HOSTNAME}',
    )
else:
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:8000',
        'http://127.0.0.1:8000',
    )

# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'quantummanagementapp.views.auth0.auth0backend.Auth0',
}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# For Testing, to persist session cookies between redirect when redirecting user from login page.
#  - Set to false for dev on localhost
if ENVIRONMENT == "production":
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # If this is set to True, the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent with an HTTPS connection
    CSRF_COOKIE_HTTPONLY = True
    # Use with Ngnix configuration
    # SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
    # https://docs.djangoproject.com/en/3.2/ref/settings/#session-cookie-domain
    SESSION_COOKIE_DOMAIN = "appspot.com"
    # Whether to store the CSRF token in the user’s session instead of in a cookie. It requires the use of django.contrib.sessions
    CSRF_USE_SESSIONS = False
    SESSION_SAVE_EVERY_REQUEST = True
    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
    SESSION_COOKIE_SECURE = True
else:
    SESSION_COOKIE_SECURE = False
    #SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = False
    # If this is set to True, the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent with an HTTPS connection
    # CSRF_COOKIE_HTTPONLY = False
    # Use with Ngnix configuration
    # SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
    # https://docs.djangoproject.com/en/3.2/ref/settings/#session-cookie-domain
    #SESSION_COOKIE_DOMAIN = "appspot.com"
    # Whether to store the CSRF token in the user’s session instead of in a cookie. It requires the use of django.contrib.sessions
    #CSRF_USE_SESSIONS = False
    #SESSION_SAVE_EVERY_REQUEST = True
    #SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
    #SESSION_COOKIE_SECURE = True


# https://docs.djangoproject.com/en/3.2/ref/contrib/sites/#module-django.contrib.sites
# SITE_ID = 1

if ENVIRONMENT == "production":
    CSRF_TRUSTED_ORIGINS = [
        'https://{QUANTUMMANAGEMENT_BASE_HOSTNAME}',
        'https://dev-405n1e6w.auth0.com'
    ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

LOGIN_URL = 'login/'
LOGIN_REDIRECT_URL = '/login/home'
LOGOUT_URL = 'logout/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

###### Google OAuth2
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env.get_value("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env.get_value("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
GOOGLE_OAUTH2_CLIENT_SECRETS_JSON = env.get_value("GOOGLE_OAUTH2_CLIENT_SECRETS_JSON")

###### FaceBook OAuth
SOCIAL_AUTH_FACEBOOK_KEY = env.get_value("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = env.get_value("SOCIAL_AUTH_FACEBOOK_SECRET")
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email, picture.type(large), link'
}

SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]


##### Auth0
SOCIAL_AUTH_TRAILING_SLASH = False  # Remove trailing slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = env.get_value("SOCIAL_AUTH_AUTH0_DOMAIN")
SOCIAL_AUTH_AUTH0_KEY = env.get_value("SOCIAL_AUTH_AUTH0_KEY")
SOCIAL_AUTH_AUTH0_SECRET = env.get_value("SOCIAL_AUTH_AUTH0_SECRET")
SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email'
]


###### LinkedIn OAuth
SOCIAL_AUTH_LINKEDIN_KEY = env.get_value("SOCIAL_AUTH_LINKEDIN_KEY")
SOCIAL_AUTH_LINKEDIN_SECRET = env.get_value("SOCIAL_AUTH_LINKEDIN_SECRET")


SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'last_name', 'email']

# Added for registration form email field
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Email verification
# https://django-allauth.readthedocs.io/en/latest/views.html#e-mail-verification
# https://django-allauth.readthedocs.io/en/latest/views.html#e-mails-management-account-email
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'optional'
# SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = False
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'None'
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'None'

SAFE_DELETE_INTERPRET_UNDELETED_OBJECTS_AS_CREATED = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

FIXTURE_DIRS = os.path.join(BASE_DIR, "quantummanagementapp/fixtures/")

# Setting Django's primary key type creation (this will exempt migrations)
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
