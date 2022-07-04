from django.contrib import admin
from django.urls import path

from bistro_app import views
# from bistro_app.views import hello


urlpatterns = [

    path('', views.home, name='home'),
    # path('hello/', hello),
    path('ingredients/',views.IngredientsView.as_view(), name='ingredients'),
    # path('recipe/', name='recipe'),
    # path('menu/', name='menu'),
    # path('order/', name='order'),
]
