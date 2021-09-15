import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "broma_config.settings.local")

django_asgi_app = get_asgi_application()

import conversations.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from conversations.middlewares import ConversationUserSessionMiddlewareStack

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": ConversationUserSessionMiddlewareStack(
            URLRouter(conversations.routing.websocket_urlpatterns),
        ),
    }
)
