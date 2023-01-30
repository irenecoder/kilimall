from django.contrib import admin
from .models import Orders

# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['created_date', ]
