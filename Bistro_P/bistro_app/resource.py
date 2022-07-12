from import_export import resources
from .models import Recipe, Ingredient


class ReportResourceRecipe(resources.ModelResource):

    class Meta:
        model = Recipe


class ReportResourceIngredient(resources.ModelResource):

    class Meta:
        model = Ingredient