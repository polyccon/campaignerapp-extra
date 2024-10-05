from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import (
    models,
    transaction,
)
from django.db.models import (
    JSONField,
    Q,
)

from campaignerapi.validators import date_is_present_or_future
from campaignerapi.tasks import send_email_task


class Messages(models.Model):
    class Meta:
        ordering = ("id",)

    subject = models.CharField(max_length=300, blank=True, null=True)
    body = JSONField(default=dict)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        editable=False,
        related_name="messages",
    )
    sending_datetime = models.DateTimeField(
        null=True, validators=[date_is_present_or_future]
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def save(self, *args, **kwargs):
        super().save(**kwargs)
        send_email_task()
