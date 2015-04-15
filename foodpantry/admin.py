from django.contrib import admin

from foodpantry.models import FoodGroup, FoodItem

admin.site.register(FoodGroup)
admin.site.register(FoodItem)
