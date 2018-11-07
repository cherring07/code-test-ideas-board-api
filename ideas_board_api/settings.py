import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',))
APP_PATH = os.path.join(ROOT_PATH, '')
sys.path.insert(0, APP_PATH)

SECRET_KEY = os.environ['SECRET_KEY']

INSTALLED_APPS = [
    # 'letsencrypt',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ideas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ideas_board_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ideas_board_api.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


if(sys.path[0].find('ideas_board_api_prod_api') is not -1):
    DEBUG = False
    PROD = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE  = True
    CSRF_COOKIE_SECURE = True
    ALLOWED_HOSTS = ['enter domain']

DEBUG = True
PROD = False
ALLOWED_HOSTS = ['127.0.0.1']
STATIC_ROOT = ROOT_PATH + '/docroot/static/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = './docroot/media/'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE  = False
CSRF_COOKIE_SECURE = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_DIRS = (
    BASE_DIR + '/static',
)
