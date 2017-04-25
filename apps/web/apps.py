from django.apps import AppConfig
from material.frontend.apps import ModuleMixin

class WebConfig(ModuleMixin, AppConfig):
    name = 'web'
