from django.contrib import admin

# Register your models here.
from mainapp.models import Category, Plant


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PlantAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'place_of_purchase', 'price',)


admin.site.register(Plant, PlantAdmin)
admin.site.register(Category, CategoryAdmin)
