from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Tshirt, Order, Customer

class TshirtAdmin(admin.ModelAdmin):
    fields = ('tshirtid', 'name', 'size', 'price', 'colour')

admin.site.register(Tshirt, TshirtAdmin)


class OrderAdmin(admin.ModelAdmin):
    fields = ('orderid', 'customer', 'tshirt', 'qty', 'amount')

admin.site.register(Order, OrderAdmin)


class CustomerAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'address', 'contact')

admin.site.register(Customer, CustomerAdmin)