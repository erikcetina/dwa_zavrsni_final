from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView
from django.views.generic import View
from main.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import DjelatnikLoginForm, DjelatnikCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView




class HomePage(TemplateView):
    template_name = 'base.html'
    form = DjelatnikLoginForm
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("main:all"))
        return super(HomePage, self).dispatch(request, *args, **kwargs)


class DjelatnikList(ListView):
    template_name = 'main/djelatnik_list.html'
    model = Djelatnik

class ProstorijaList(ListView):
    model = Prostorija

class OpremaList(ListView):
    model = Oprema

class RezervacijaList(ListView):
    model = Rezervacija

class LoginPageView(LoginView):
    template_name = 'authentication/login.html'
    next_page = "/"
    
class UserLogoutView(LogoutView):
    next_page = "/"
    def signout(request):
        logout(request)
        
class SignUpView(CreateView):
    form_class = DjelatnikCreationForm
    next_page = "/login"
    template_name = "authentication/signup.html"
    success_url = "/login"



class RezervacijaBaseView(LoginRequiredMixin, View):
    model = Rezervacija
    fields = '__all__'
    success_url = reverse_lazy('main:all')
    login_url = '/login'
    #redirect_field_name = 'redirect_to'

class RezervacijaListView(RezervacijaBaseView, ListView):
    """View to list all films.
    Use the 'film_list' variable in the template
    to access all Film objects"""

class RezervacijaDetailView(RezervacijaBaseView, DetailView):
    template_name = 'main/rezervacija_detail.html'
    """View to list the details from one film.
    Use the 'film' variable in the template to access
    the specific film here and in the Views below"""

class RezervacijaCreateView(RezervacijaBaseView, CreateView):
    """View to create a new film"""

    

class RezervacijaUpdateView(RezervacijaBaseView, UpdateView):
    """View to update a film"""

class RezervacijaDeleteView(RezervacijaBaseView, DeleteView):
    """View to delete a film""" 

