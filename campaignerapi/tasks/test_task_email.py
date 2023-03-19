"""Celery tasks for sending emails
"""

import os
import datetime as dt
from campaignerapi.models import Messages
from celery import shared_task
import logging

import pytz
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

from campaignerapi.celery import app

from campaignerapi.util.other import (
    mask_email,
    snake_case_to_title_human,
)

LOGGER = logging.getLogger(__name__)


def send_email(subject, email_address, email_html_content):
    """Send email contents to a given email address

    :param subject: email subject
    :param email_address: single email address
    :param email_html_content: HTML content
    :return:
    """

    mail = EmailMultiAlternatives(
        subject=subject,
        from_email=os.getenv("DEFAULT_FROM_EMAIL"),
        to=[email_address],
    )

    mail.attach_alternative(email_html_content, "text/html")
    mail.send()

    LOGGER.info(
        "Email Sent",
        extra={
            "ids": {
                "email": mask_email(email_address),
            }
        },
    )


def render_email_template(template_path, title, body):
    context = {"title": title, "body": body}

    return render_to_string(template_path, context)


@app.task
def send_email_task():
    # TODO: add this as a field in database
    subject = "TEST SUBJECT"

    messages = Messages.objects.all()

    for message in messages:
        # TODO: improve naming description and title is the same, summary and body also
        email_html_content = render_email_template(
            "email/test_email.html", message.description, message.summary
        )
        destination_email = os.getenv("DEFAULT_TO_EMAIL")
        send_email(subject, destination_email, email_html_content)
