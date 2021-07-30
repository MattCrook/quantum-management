import os
# from environ import Env




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# env = Env()
# env.read_env(env_file=os.path.join(BASE_DIR, '.env.dev'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = '5utjtqz%(md_zyoyiewi7t@@vk7tg$o@u-ao(69k_l5itd50z!'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = int(os.environ.get("DEBUG", default=0))



ALLOWED_HOSTS = ['localhost', '8000', '127.0.0.1']
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


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



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quantumdb',
        'USER': 'matthewcrook',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
#         "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
#         "USER": os.environ.get("SQL_USER", "user"),
#         "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
#         "HOST": os.environ.get("SQL_HOST", "localhost"),
#         "PORT": os.environ.get("SQL_PORT", "5432"),
#     }
# }



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

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://127.0.0.1:8000',
)



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
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '567594519343-1relp58adg0suplc4naq8n9ribamoca4.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'o28VhmDO9gyz1YhQi-phQj-l'
GOOGLE_OAUTH2_CLIENT_SECRETS_JSON = 'client_secrets.json'


###### FaceBook OAuth
SOCIAL_AUTH_FACEBOOK_KEY = '373817170537484'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c964d38aeebe4728fa8c0b3346608462'
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
SOCIAL_AUTH_AUTH0_DOMAIN = 'dev-405n1e6w.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = '7ECrruuGVEjBOGcGyTqbRPvg4hQFXqRa'
SOCIAL_AUTH_AUTH0_SECRET = 'yJj0SzZCHm5s9WeAOCPOyjMjW9Rg9x7wtb6qqTMeqq7mcOpuN91vnbZ1lqKJ-fJS'
SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email'
]


###### LinkedIn OAuth
# SOCIAL_AUTH_LINKEDIN_KEY = 'foobar'
# SOCIAL_AUTH_LINKEDIN_SECRET = 'bazqux'


SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'last_name', 'email']

# Added for registration form email field
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




SAFE_DELETE_INTERPRET_UNDELETED_OBJECTS_AS_CREATED = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

FIXTURE_DIRS = os.path.join(BASE_DIR, "quantummanagementapp/fixtures/")
