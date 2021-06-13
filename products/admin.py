from django.contrib import admin
from django.contrib import admin
from .models import Product, Category, Color

# Register your models here.

"""
Register Product, Categiory and Color models
Customize fields being displayed in admin view
"""


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ColorInline(admin.StackedInline):
    model = Color
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Required', {'fields': ['name',
                                 'description',
                                 'category',
                                 'price',
                                 'release_date',
                                 'many_colors', ]}),
        ('Product Images', {'fields': ['main_pic',
                                       'pic2',
                                       'pic3',
                                       'pic4'], }),
    ]
    inlines = [ColorInline]
    list_display = (
        'name',
        'category',
        'price',
        'added_date',
        'release_date',
    )
    date_hierarchy = 'added_date'


admin.site.register(Product, ProductAdmin)