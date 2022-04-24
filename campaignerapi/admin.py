import csv
import datetime as dt
import logging

from django import forms
from django.conf import settings
from django.contrib import (
    admin,
    messages,
)
from django.contrib.admin.helpers import ActionForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone
from django.utils.html import format_html
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.reverse import reverse

from campaignerapi.models import Messages


class AdminSite(admin.AdminSite):
    pass


admin.site.login = AdminSite().login
admin.autodiscover()


logger = logging.getLogger(__name__)


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ("description", "summary", "user")
