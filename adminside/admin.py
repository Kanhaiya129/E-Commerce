from django.contrib import admin
from .models import Items, Categories, ItemImage


class ItemimageInline(admin.StackedInline):
    model = ItemImage
    extra = 1


@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemimageInline]
    list_display = [
        "name",
    ]


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
