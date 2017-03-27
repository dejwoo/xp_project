# Import some utility functions
from os.path import join
# Fetch our common settings
from xp_project.settings.common import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "xp_project",
    }
}

# ##### APPLICATION CONFIGURATION #########################


INSTALLED_APPS = DEFAULT_APPS + [
    "api",
    "web"
]
