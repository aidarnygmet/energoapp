from django.apps import AppConfig
from channels.routing import ProtocolTypeRouter, URLRouter

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    def ready(self):        
        import app.signals
class ChannelsAppConfig(AppConfig, ProtocolTypeRouter):
    pass