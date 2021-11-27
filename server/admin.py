import logging

from django import forms
from django.conf import settings
from django.contrib import (
    admin,
    messages,
)

class AdminSite(admin.AdminSite):
    login_template = "microsoft/admin_login.html"


admin.site.login = AdminSite().login
admin.autodiscover()

logger = logging.getLogger(__name__)
