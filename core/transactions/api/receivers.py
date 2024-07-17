from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Checkout, Hold
from books.models import Book


@receiver(post_save, sender=Checkout)
def update_book_availabilty(sender, instance, **kwargs):
    if instance.is_returned:
        # removing the first user waiting for the book from hold table and add it to checkout table
        hold_book = Hold.objects.filter(book=instance.book).first()
        
        if hold_book:
            Checkout.objects.create(
                start_time=hold_book.start_time,
                end_time=hold_book.end_time,
                book=hold_book.book,
                customer=hold_book.customer,
                is_returned=False,
            )
            hold_book.delete()


        # changing the book availablity to true if no one is on the hold list
        # book = instance.book
        # book.is_available = True
        # book.save()
