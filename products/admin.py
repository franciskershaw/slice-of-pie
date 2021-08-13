from django.contrib import admin
from .models import Product, Angle, Level, Material


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'level',
        'material',
        'angle',
        'price',
        'image_1',
        'image_2',
    )

    ordering = ('sku',)


class AngleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Angle, AngleAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Material, MaterialAdmin)
