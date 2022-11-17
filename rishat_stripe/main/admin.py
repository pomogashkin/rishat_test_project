from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-nothing-'


admin.site.register(Item, ItemAdmin)
