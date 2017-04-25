from django.apps import AppConfig
from apps.api.signals import MqttClient

class ApiConfig(AppConfig):
    name = 'apps.api'
    verbose_name = 'Project Noe API app'
    def ready(self):
        self.mqtt = MqttClient();

