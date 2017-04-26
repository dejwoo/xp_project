# Import some utility functions
import os
# Fetch our common settings
from xp_project.settings.common import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = False

# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': os.environ.get("POSTGRESQL_USER"),
        'PASSWORD': os.environ.get("POSTGRESQL_PASSWORD"),
        'HOST': os.environ.get("POSTGRESQL_HOST"),
        'PORT': os.environ.get("POSTGRESQL_PORT"),
        'NAME': os.environ.get("POSTGRESQL_DBNAME")
    }
}

# ##### APPLICATION CONFIGURATION #########################


INSTALLED_APPS = DEFAULT_APPS + [
    "apps.api",
    "apps.web"
]
