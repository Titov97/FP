from django.contrib import admin
#TODO RADU - admin

# Register your models here.
from Bistro_P.bistro_app.models import *

admin.site.register(Ingredients)
admin.site.register(Recipe)
admin.site.register(Menu)
admin.site.register(Order)