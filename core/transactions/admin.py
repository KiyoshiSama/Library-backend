from django.contrib import admin
from transactions.models import Checkout, Hold

admin.site.register(Checkout)
admin.site.register(Hold)
