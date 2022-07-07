from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from bistro_app import views
# from bistro_app.views import hello
from bistro_app.views import contact_view, MyPasswordChangeView,  search_view

urlpatterns = [

    path('', views.home, name='home'),
    # path('hello/', hello),
    path('ingredients/', views.IngredientsView.as_view(), name='ingredients'),
    path('recipes/', views.RecipeView.as_view(), name='recipes'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('contact/', contact_view, name='contact'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/change_pass/', views.MyPasswordChangeView.as_view(), name='change_pass'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', search_view, name="search_results"),
]