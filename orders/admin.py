from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'order_date')
    search_field = ('customer_name',)
    list_filter = ('order_date' ,)