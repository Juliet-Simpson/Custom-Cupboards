from django.contrib import admin
from .models import Material, Cupboard, Type

# Register your models here.


class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
        'price_per_m2',
    )

    ordering = ('display_name',)


class TypeAdmin(admin.ModelAdmin):

    ordering = ('name',)


class CupboardAdmin(admin.ModelAdmin):
    list_display = (
        'design_id',
        'name',
        'type',
        'material',
        'design_surcharge',
        'example_price',
        'main_image'
    )

    ordering = ('design_id',)


admin.site.register(Material, MaterialAdmin)
admin.site.register(Cupboard, CupboardAdmin)
admin.site.register(Type, TypeAdmin)
