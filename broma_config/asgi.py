import os

import chats.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from chats.middlewares import ConversationUserSessionMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "broma_config.settings.local")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": ConversationUserSessionMiddlewareStack(
            URLRouter(chats.routing.websocket_urlpatterns),
        ),
    }
)
