from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','cost_per_item','stock_quantity','volume']
    fields = ['name','description','cost_per_item','stock_quantity']

admin.site.register( Product , ProductAdmin )
