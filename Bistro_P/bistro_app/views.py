from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import ContactForm, SignUpForm
from django.views.generic import CreateView, ListView
from django.views import View

from bistro_app.models import Ingredient, Recipe, SalesMenu, Order


# -----cart------
# from django.shortcuts import render, get_object_or_404
# from .models import CartCategory, CartProduct
# from .forms import CartAddProductForm
# -------------

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
        return render(request, template_name="menu.html", context={"menu": SalesMenu.objects.all()})


class OrderView(View):
    def get(self, request):
        return render(request, template_name="order.html", context={"orders": Order.objects.all()})


def contact_view(request):
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


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')


class SignUpView(CreateView):
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'registration/change_pass.html'
    success_url = reverse_lazy('login')


# class MyLoView(LoginView):
#     template_name = 'registration/change_pass.html'
#     success_url = reverse_lazy('login')

class MyLogoutView(LogoutView):
    template_name = 'registration/logout.html'
    success_url = reverse_lazy('index')


def bar_view(request):
    query = request.GET.get('query', '')
    return render(request, "bar.html", {"query": query})


def food_view(request):
    query = request.GET.get('query', '')
    return render(request, "food.html", {"query": query})


def deserts_view(request):
    query = request.GET.get('query', '')
    return render(request, "deserts.html", {"query": query})


# class FoodView(CreateView):
#     template_name = 'food.html'
#
#
# class DesertsView(CreateView):
#     template_name = 'deserts.html'


def search_view(request):
    results = []
    query = ""
    if request.method == "GET":
        query = request.GET.get("q")
        if query == " ":
            query = "No results"
        results = Recipe.objects.filter(Q(ingredients__ingredient__name__icontains=query) | Q(name__icontains=query))
    return render(request, "search_results.html", {"query": query, "results": results})


@login_required
def open_cart_view(request):
    return render(request, "open_cart.html", {'cart': get_open_cart(request)})


def get_open_cart(request):
    open_cart = Order.objects.filter(user=request.user, status='open').first()
    if open_cart is None:
        open_cart = Order.objects.create(user=request.user, status='open')
    return open_cart


# --------
def check_out(request):
    return render(request, template_name='checkout.html')

def cancel_order(request):
    return render(request, template_name='cancel.html')

def succes_order(request):
    return render(request, template_name='success.html')


def special_view(request):
    query = request.GET.get('query', '')
    return render(request, "special.html", {"query": query})

