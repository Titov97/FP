from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from bistro_app.models import Ingredient, Recipe
from .resource import ReportResourceIngredient, ReportResourceRecipe
# Register your models here.
# from Bistro_P.bistro_app.models import *
from bistro_app.models import *


class ImportIngredientAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceIngredient


class ImportRecipeAdmin2(ImportExportModelAdmin):
    resource_class = ReportResourceRecipe


# admin.site.register(Ingredient)

# admin.site.register(Recipe)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(RecipeIngredient)
admin.site.register(Ingredient, ImportIngredientAdmin)
admin.site.register(Recipe, ImportRecipeAdmin2)
