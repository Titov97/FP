from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.views import View

from bistro_app.models import Ingredient, Recipe, Menu, Order


# def hello(request):
#     query = request.GET.get('query', '')
#     return HttpResponse('Hello')
def home(request):
    return render(request, template_name='home.html')


class IngredientsView(View):
    def get(self, request):
        return render(request, template_name="ingredients.html", context={"ingredients": Ingredient.objects.all()})


class RecipeView(View):
    def get(self, request):
        return render(request, template_name="recipes.html", context={"recipes": Recipe.objects.all()})


class MenuView(View):
    def get(self, request):
        return render(request, template_name="menu.html", context={"menu": Menu.objects.all()})


class OrderView(View):
    def get(self, request):
        return render(request, template_name="order.html", context={"orders": Order.objects.all()})


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['bistro.p2022@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
