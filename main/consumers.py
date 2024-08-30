import aioredis
import logging
from django.shortcuts import get_object_or_404
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from . import models

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncJsonWebsocketConsumer):
    EMPLOYEE = 2
    CLIENT = 1
    
    def get_user_type(self, user, order_id):
        order = get_object_or_404(models.Order, pk=order_id)
        
        if user.is_employee:
            order.last_spoken_to = user
            order.save()
            return ChatConsumer.EMPLOYEE
        elif order.user == user:
            return ChatConsumer.CLIENT
        else:
            return None
    
    async def connect(self):
        self.order_id = self.scope['url_route']['kwargs'][
            'order_id']
        self.room_group_name = (
            'customer_service_%s' % self.order_id)
        authorized = False
        if self.scope['user'].is_anonymous:
            await self.close()
        
        user_type = await database_sync_to_async(
            self.get_user_type
        )(self.scope['user'], self.order_id)

