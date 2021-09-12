from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    username = models.CharField(_("username"), max_length=25, unique=True, blank=False, null=False)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
