"""
ASGI config for teploapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.urls import path
import os

from django.core.asgi import get_asgi_application
from app.consumer import GraphConsumer
import app.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teploapp.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': URLRouter(
            app.routing.websocket_urlpatterns
        )
})
