from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app import consumer

websocket_urlpatterns = [
    path('ws/graph/', consumer.GraphConsumer.as_asgi()),
    # Add other websocket URL patterns here if you have more consumers
]