from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from bistro_app.models import Ingredient, Recipe, Menu, Order


def hello(request):
    query = request.GET.get('query', '')
    return HttpResponse('Hello')


class IngredientsView(View):
    def get(self, request):
        return render(request, template_name="ingredients.html", context={"ingredients": Ingredient.objects.all()})


class RecipeView(View):
    def get(self, request):
        return render(request, template_name="recipe.html", context={"recipes": Recipe.objects.all()})


class MenuView(View):
    def get(self, request):
        return render(request, template_name="menu.html", context={"menu": Menu.objects.all()})


class OrderView(View):
    def get(self, request):
        return render(request, template_name="order.html", context={"orders": Order.objects.all()})
