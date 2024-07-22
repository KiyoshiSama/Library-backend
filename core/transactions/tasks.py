from mail_templated import EmailMessage
from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils.timezone import now , timedelta
from transactions.models import Checkout

@shared_task
def send_borrow_ending_alert():
    two_days_from_now = now().date() + timedelta(days=2)
    soon_ending_checkouts = Checkout.objects.filter(
        end_time__lte=two_days_from_now, is_returned=False
    )
    for checkout in soon_ending_checkouts:
            email_obj = EmailMessage(
                "email/reserve_ending_alert.tpl",
                {
                    "days_remaining": (checkout.end_time - now().date()).days,
                    "user_first_name": checkout.customer.first_name,
                },
                "admin@admin.com",
                to=[checkout.customer.email],
            )
            email_obj.send()
