from django.contrib import admin
from.forms import StockCreateForm

# Register your models here.

from .models import Stock

class StockCreateAddmin(admin.ModelAdmin):
    list_display = ['category','item_name','quantity']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category','item_name']

admin.site.register(Stock, StockCreateAddmin)