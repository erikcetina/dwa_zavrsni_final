# import form class from django
from django import forms  
from django.contrib.auth.forms import UserCreationForm

# import GeeksModel from models.py
from .models import Djelatnik, Prostorija, Oprema, Rezervacija
  
# create a ModelForm

class DjelatnikCreationForm(UserCreationForm):
    
    class Meta:
        model = Djelatnik
        fields = ["Ime", "Prezime", "OIB", "email", "titula"]
        
class DjelatnikLoginForm(forms.ModelForm):

    class Meta:
        model = Djelatnik
        fields = ["email", "password"]
