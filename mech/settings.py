# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


STATIC_PATH = os.path.join(os.path.expanduser('~'), 'domains/swordsman.su')

# Django settings for mech project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dmitry Krupin', 'krupin.dv19@gmail.com'),
)


#'NAME': os.path.join(PROJECT_PATH, "mech_db.sqlite"),

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'verseau_swordsman',
        'USER': 'verseau', # Not used with sqlite3.
        'PASSWORD': 'v123456', # Not used with sqlite3.
        'HOST': '127.0.0.1', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': 3306, # Set to empty string for default. Not used with sqlite3.
    }
}


#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = '/home/dmitry/remote_projects/tmp/swordsman_messages' # change this to a proper location

#EMAIL_FILE_PATH = os.path.join(os.path.expanduser('~'), 'tmp/swordsman_emails')

EMAIL_HOST = "smtp.test.ru"
EMAIL_PORT = 587
EMAIL_HOST_USER = "contact@swordsman.su"
EMAIL_HOST_PASSWORD = "v123456"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "contact@swordsman.su"


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["http://swordsman.su"]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU' #ru-RU
#LOCALE_NAME = 'ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(STATIC_PATH, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(STATIC_PATH, "root_static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(STATIC_ROOT, "mech"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    #'dajaxice.finders.DajaxiceFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'eo-rlhcf@orjjajdwa__#1@kpk9#phdbably!tz&*0v%pq6hu8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    #'cms.middleware.toolbar.ToolbarMiddleware',
    #'cms.middleware.language.LanguageCookieMiddleware',

    #'middleware.user.RequireLoginMiddleware',
    'middleware.user.RequirePermissionMiddleware',

)

ROOT_URLCONF = 'mech.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mech.wsgi.application'


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'




RESTRICTED_URLS = (
    (r'/photologue/(.*)$', 'mech.view_gallery'),
    (r'/video/(.*)$', 'videos.view_video'),
#    (r'/statistic/(.*)$', 'training.view_statistic'),
    (r'/arendapokupka-trenirovochnogo-snaryazheniya/(.*)$', 'training.view_statistic'),
    
    
    
)

RESTRICTED_URLS_EXCEPTIONS = (
    r'/login(.*)$', 
    r'/logout(.*)$',
)



ACCOUNT_ACTIVATION_DAYS=10


VIDEO_WIDTH=400
VIDEO_HEIGHT=300
VIDEO_FULLSCREEN=False


CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_6_blocks.html', 'Template 6 sections'),
    ('template_3_cols.html', 'Template 3 columns'),
)




CMS_LANGUAGES = {
    1: [
        {
            'code': 'ru',
            'name': gettext('Russian'),
            #'fallbacks': ['en'],
            'public': True,
        },
    ],
        
                 
    'default': {
        'fallbacks': ['ru'],
        'redirect_on_fallback':True,
        'public': True,
        'hide_untranslated': False,
    }
}


#CMS_MENU_TITLE_OVERWRITE = True



INSTALLED_APPS = (
   
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    
    'registration',
    'middleware',
    'mech',
    'videos',
    'training',     #статистика соревнований
    'photologue',

    
    
    "filer", "easy_thumbnails", 
    
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    
    #"cmsplugin_filer_html5video",

    'cms', #django CMS itself
    'mptt', #utilities for implementing a modified pre-order traversal tree
    'menus', #helper for model independent hierarchical website navigation
    'south', #intelligent schema and data migrations
    'sekizai', #for javascript and css management


    #'cms.plugins.file',
    #'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    #'cms.plugins.snippet',
    #'cms.plugins.teaser',
    'cms.plugins.text',
    #'cms.plugins.video',
    'cms.plugins.inherit',
)



#for django-filer
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)



try:
    from photologue import PHOTOLOGUE_TEMPLATE_DIR    #photologue-2.6.1
except Exception:
    from photologue import PHOTOLOGUE_APP_DIR as PHOTOLOGUE_TEMPLATE_DIR #photologue-2.1



TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "templates"),

    PHOTOLOGUE_TEMPLATE_DIR,
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',

    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',

     #"djangohelper.context_processors.ctx_config",
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
