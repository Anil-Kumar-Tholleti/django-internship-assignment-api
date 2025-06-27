
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        subject='Welcome to the Internship Project',
        message='Thank you for registering!',
        from_email='your_email@example.com',  # Update if needed
        recipient_list=[user_email],
    )

