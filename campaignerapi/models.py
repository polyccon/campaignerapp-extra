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


class Messages(models.Model):
    class Meta:
        ordering = ("id",)

    # TODO: Add sending_date
    description = models.CharField(max_length=300, blank=True, null=True)
    summary = JSONField(default=dict)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        editable=False,
        related_name="messages",
    )
