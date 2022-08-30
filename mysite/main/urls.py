from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.HomePage.as_view(), name="homepage"),
    path('login', views.LoginPageView.as_view(), name='login'),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("logout", views.UserLogoutView.as_view(), name="logout"),
    path('Djelatnik', views.DjelatnikList.as_view(), name='DjelatnikList'),
    path('Prostorija', views.ProstorijaList.as_view(), name='ProstorijaList'),
    path('Oprema', views.OpremaList.as_view(), name='OpremaList'),
    path('Rezervacija', views.RezervacijaList.as_view(), name='RezervacijaList'),

    path('rezervacije', views.RezervacijaListView.as_view(), name='all'),
    path('rezervacije/<int:pk>/', views.RezervacijaDetailView.as_view(), name='rezervacije_detail'),
    path('rezervacije/create/', views.RezervacijaCreateView.as_view(), name='rezervacije_create'),
    path('rezervacije/<int:pk>/update/', views.RezervacijaUpdateView.as_view(), name='rezervacije_update'),
    path('rezervacije/<int:pk>/delete/', views.RezervacijaDeleteView.as_view(), name='rezervacije_delete'), 
]

