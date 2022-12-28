from django.contrib import admin
from .models import Product,Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','category','posted']
    list_filter = ['name','slug']
