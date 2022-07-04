from django.contrib.auth.models import User
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    quantity_stock = models.FloatField()
    unit = models.CharField(max_length=128)
    price_unit = models.FloatField()
    min_stock = models.FloatField()
    alert_stock = models.FloatField()
    remarks = models.CharField(max_length=128)
    lot = models.CharField(max_length=128)
    entry_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.name} {self.quantity_stock}{self.unit}"


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.ingredient.name} {self.quantity}{self.ingredient.unit}"


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    # created_by = models.CharField(max_length=128)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ingredients = models.ManyToManyField(RecipeIngredient)
    sale_price = models.FloatField()

    def production_price(self):
        # total_cost = 0
        # for recipe_ingredient in self.ingredients.all():
        #     total_cost += recipe_ingredient.ingredient.price_unit * recipe_ingredient.quantity
        # return total_cost
        return (recipe_ingredient.ingredient.price_unit * recipe_ingredient.quantity for recipe_ingredient in
                self.ingredients.all())


class Menu(models.Model):
    menu_name = models.CharField(max_length=255)
    sale_price = models.FloatField()


class MenuItem(models.Model):
    recipe = models.ForeignKey(RecipeIngredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe} {self.quantity}"


class Order(models.Model):
    #status = models.Choices #TODO Radu
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class OrderItem(models.Model):
    recipe = models.ForeignKey(RecipeIngredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

