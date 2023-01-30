from django.contrib import admin
from .models import Orders

# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','city','email','address',
                    'paid','updated_date','postal_code','created_date', ]
    list_filter = ['paid','created_date','updated_date']
    inlines = ['OrderItemInline']

class OrderItemInline(admin.TabularInline):
    model = Orders
    raw_id_fields = ['product']
