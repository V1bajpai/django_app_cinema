from django.contrib import admin

# Register your models here.
from app.models import Home, Customer, BookTicket

admin.site.register(Home)
admin.site.register(Customer)
admin.site.register(BookTicket)
