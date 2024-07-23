import random
from mail_templated import EmailMessage
from celery import shared_task
from django.core.cache import cache

@shared_task
def send_verification_code_task(user_id, email):
    try:
        verification_code = str(random.randint(10000, 99999))
        cache.set(str(user_id), verification_code, 120)
        email_obj = EmailMessage(
            "email/activation_email.tpl",
            {"verification_code": verification_code},
            "admin@admin.com",
            to=[email],
        )
        email_obj.send()
        return True
    except Exception as e:
        print(f"Failed to send activation email: {str(e)}")
        return False
