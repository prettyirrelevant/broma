import uuid
from typing import Iterable, Optional

from accounts.models import User
from django.db import IntegrityError, models
from django.utils.translation import gettext_lazy as _


class Conversation(models.Model):
    """
    This model represents a room for chatting, video call and game between two users.
    """

    id = models.UUIDField(_("conversation id"), primary_key=True, default=uuid.uuid4)

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_conversations",
    )
    invitee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="joined_conversations",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")

    content = models.TextField(_("content"), blank=False, null=False)
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)
