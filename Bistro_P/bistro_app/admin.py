from django.contrib import admin

#TODO RADU - admin

# Register your models here.
# from Bistro_P.bistro_app.models import *
from bistro_app.models import *

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(RecipeIngredient)

