from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from bistro_app import views
# from bistro_app.views import hello
from bistro_app.views import contact_view, MyPasswordChangeView,  search_view

urlpatterns = [

    path('', views.home, name='index'),
    path('ingredients/', views.IngredientsView.as_view(), name='ingredients'),
    path('recipes/', views.RecipeView.as_view(), name='recipes'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('contact/', contact_view, name='contact'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/change_pass/', MyPasswordChangeView.as_view(), name='change_pass'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', search_view, name="search_results"),
    path('cart/', views.open_cart_view, name="open_cart"),
    path('special/', views.special_view, name="special"),
    path('checkout/', views.check_out, name="checkout"),
    path('cancel/', views.cancel_order, name="cancel"),
    path('succes/', views.succes_order, name="succes"),
]
