from django.contrib import admin
from .models import Cars, Clients, Orders, ExOrders


admin.site.register(Clients)
admin.site.register(Cars)
admin.site.register(Orders)
admin.site.register(ExOrders)
# Register your models here.
