import json

from channels.db import database_sync_to_async
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from redis import StrictRedis

from .models import Conversation, User

redis = StrictRedis.from_url(url=settings.REDIS_URL, encoding="utf-8", decode_responses=True)


@database_sync_to_async
def validate_connection(conversation, user) -> None:
    if not conversation or not user:
        raise DenyConnection()

    if user not in [conversation.creator, conversation.invitee]:
        raise DenyConnection()


class ConversationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_id: str = self.scope["url_route"]["kwargs"]["id"]
        self.conversation_room: str = f"conversation_{self.conversation_id}"

        self.user: User = self.scope["user"]
        conversation: Conversation = self.scope["conversation"]

        await self.accept("Token")
        await validate_connection(conversation, self.user)

        redis.sadd(f"conversation:{self.conversation_id}", self.user.username)
        await self.channel_layer.group_add(self.conversation_room, self.channel_name)

        await self.channel_layer.group_send(
            self.conversation_room,
            {
                "type": "conversations.online_users",
                "data": list(redis.smembers(f"conversation:{self.conversation_id}")),
            },
        )

    async def disconnect(self, code):
        redis.srem(f"conversation:{self.conversation_id}", self.user.username)

        await self.channel_layer.group_send(
            self.conversation_room,
            {
                "type": "conversations.online_users",
                "data": list(redis.smembers(f"conversation:{self.conversation_id}")),
            },
        )

        await self.channel_layer.group_discard(self.conversation_room, self.channel_name)

    async def receive(self, text_data, bytes_data=None):
        text_data_json = json.loads(text_data)

        event = text_data_json["event"]

        if event == "conversations.game":
            await self.channel_layer.group_send(
                self.conversation_room,
                {
                    "type": event,
                    "data": text_data_json,
                },
            )

    async def conversations_game(self, event):
        """
        A function that handles everything as regards the tic-tac-toe game.
        """

        action = event["data"]["action"]

        if action == "START":
            members = list(redis.smembers(f"conversation:{self.conversation_id}"))
            players = [
                {"username": members[0], "choice": "X"},
                {"username": members[-1], "choice": "O"},
            ]
            await self.send(
                text_data=json.dumps(
                    {"event": "conversations.game", "action": "START", "message": players}
                )
            )
        elif action == "MOVE":
            await self.send(
                text_data=json.dumps(
                    {
                        "event": "conversations.game",
                        "action": "MOVE",
                        "message": event["data"]["message"],
                    }
                )
            )

        elif action == "END":
            await self.send(
                text_data=json.dumps(
                    {
                        "event": "conversations.game",
                        "message": event["data"]["message"],
                        "action": "END",
                    }
                ),
            )

    async def conversations_online_users(self, event):
        """
        A function that updates the active users in a conversation
        using connect/disconnect from a redis store.
        """
        users = event["data"]
        await self.send(
            text_data=json.dumps(
                {
                    "users": users,
                    "event": "conversations.online_users",
                }
            )
        )
