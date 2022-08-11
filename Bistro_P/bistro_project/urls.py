"""bistro_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap # new

import bistro_app
from bistro_app import views
from bistro_project import settings

from bistro_app.models import Recipe

info_dict = {
    'queryset': Recipe.objects.all(),
}


urlpatterns = [
   path('admin/', admin.site.urls),
   # path('', views.home, name='home'),
   path('', include('bistro_app.urls')),
   path('sitemap.xml', sitemap, # new
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

