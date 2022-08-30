from django.contrib import admin
from main.models import *

## Register your models here.
modeli = [Djelatnik, Prostorija, Oprema, Rezervacija]
admin.site.register(modeli)