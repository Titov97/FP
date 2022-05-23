from django.db import models


# Create your models here.

class Ingredients(models.Model):
    ingredients = models.CharField(max_length=128)
    quantity_stock = models.FloatField()
    unit = models.CharField(max_length=128)
    price_unit = models.FloatField()
    min_stock = models.FloatField()
    alert_stock = models.FloatField()
    remarks = models.CharField(max_length=128)
    lot = models.CharField(max_length=128)
    entry_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(null=False)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=128)
    created_by = models.CharField(max_length=128)



class Menu(models.Model):
    pass


class Order(models.Model):
    pass
