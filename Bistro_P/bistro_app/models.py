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


class Menu(models.Model):
    #manytomany recipe
    pass

class Order(models.Model):
    pass


class OrderItem(models.Model):
    pass


