from django.contrib import admin
from django.urls import path

from bistro_app import views
# from bistro_app.views import hello
from bistro_app.views import contact_view

urlpatterns = [

    path('', views.home, name='home'),
    # path('hello/', hello),
    path('ingredients/',views.IngredientsView.as_view(), name='ingredients'),
    path('recipes/', views.RecipeView.as_view(), name='recipes'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('order/', views.OrderView.as_view,  name='order'),
    path('contact/', contact_view,  name='contact'),
]
