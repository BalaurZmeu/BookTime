import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path
from main.consumers import ChatConsumer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booktime.settings")
django.setup()
django_asgi_app = get_asgi_application()



application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path("customer-service/<int:order_id>/",
                    ChatConsumer.as_asgi()
                ),
            ])
        )
    ),
})

