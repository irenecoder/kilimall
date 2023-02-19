from django.contrib import admin
from .models import Orders,OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
    'address', 'postal_code', 'city', 'paid',
    'created_date', 'updated_date']
    list_filter = ['paid', 'created_date', 'updated_date']
    inlines = [OrderItemInline]

