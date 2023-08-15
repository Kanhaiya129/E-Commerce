from django.contrib import admin
from .models import Items, Categories


@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display= [
        'name',
    ]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display= [
        'name',
    ]
