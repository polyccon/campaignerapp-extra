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

# Create your models here.


class Messages(models.Model):
    class Meta:
        ordering = ("id",)

    description = models.CharField(max_length=300, blank=True, null=True)
    summary = JSONField(default=dict)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        editable=False,
        related_name="messages",
    )
