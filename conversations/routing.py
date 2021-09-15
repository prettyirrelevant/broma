from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r"ws/conversations/<id>/", consumers.ConversationConsumer.as_asgi()),
]
