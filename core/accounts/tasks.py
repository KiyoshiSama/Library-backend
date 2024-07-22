import random
from mail_templated import EmailMessage
from celery import shared_task
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_activation_email(user_id, email):
    try:
        user = User.objects.get(id=user_id)
        verification_code = str(random.randint(10000, 99999))
        user.verification_code = verification_code
        user.save()

        email_obj = EmailMessage(
            "email/activation_email.tpl",
            {"verification_code": verification_code},
            "admin@admin.com",
            to=[email],
        )
        email_obj.send()
        return True

    except Exception as e:
        print(f"Unexpected error, try again : {str(e)}")
        return False

