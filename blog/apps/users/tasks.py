from django.conf import settings
from django.core.mail import send_mail


def send_mail_task(subject, message, email_to):
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email_to])
