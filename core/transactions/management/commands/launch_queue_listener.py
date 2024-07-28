from django.core.management.base import BaseCommand
from  transactions.logger.queue_listener import UserCreatedListener
class Command(BaseCommand):
    help = 'Launches Listener for book_borrowed message : RaabitMQ'
    def handle(self, *args, **options):
        td = UserCreatedListener()
        td.start()
        self.stdout.write("Started Consumer Thread")