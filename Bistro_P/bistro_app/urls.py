from django.contrib import admin
from django.urls import path

from bistro_app import views
from bistro_app.views import hello


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='home.html')
    path('hello/', hello),
    path('ingredients/', name='ingredients'),
    path('recipe/', name='recipe'),
    path('menu/', name='menu'),
    path('order/', name='order'),
]