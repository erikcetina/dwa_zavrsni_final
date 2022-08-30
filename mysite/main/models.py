from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.core.exceptions import ValidationError

# Create your models here.
class Djelatnik(AbstractUser):

    username = None
    Ime = models.CharField(max_length=100)
    Prezime = models.CharField(max_length=100)
    OIB = models.IntegerField(
        validators=[MinValueValidator(10000000000), MaxValueValidator(99999999999)],
    null=True)
    email = models.EmailField(unique=True)
    titule_lista = [("PR", "Profesor"), ("AS", "Asistent")]
    titula = models.CharField(max_length=100, choices=titule_lista)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.Ime


class Prostorija(models.Model):
    Broj_prostorije = models.CharField(max_length=100)
    Kat = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)])

    def __str__(self):
        return self.Broj_prostorije


class Oprema(models.Model):
    Ime_opreme = models.CharField(max_length=100)
    Cijena_opreme = models.DecimalField(max_digits=10, decimal_places=2)
    Prostorija = models.ForeignKey(Prostorija, on_delete=models.CASCADE)

    def __str__(self):
        return self.Ime_opreme


class Rezervacija(models.Model):
    Djelatnik = models.ForeignKey(Djelatnik, on_delete=models.CASCADE)
    Oprema = models.ForeignKey(Oprema, on_delete=models.CASCADE)
    Prostorija = models.ForeignKey(Prostorija, on_delete=models.CASCADE)
    Razdoblje_od = models.DateField()
    Razdoblje_do = models.DateField()

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (
            self.Djelatnik,
            "rezervacija. Od",
            self.Razdoblje_od,
            "do",
            self.Razdoblje_do,
            ". Prostorija",
            self.Prostorija,
        )

    def clean(self, *args, **kwargs):
        if self.Oprema.Prostorija != self.Prostorija:
            raise ValidationError("Oprema se ne nalazi u prostoriji.")

        Razdoblje_od_in_range = models.Q(Razdoblje_od__lte=self.Razdoblje_od, Razdoblje_do__gte=self.Razdoblje_od)
        Razdoblje_do_in_range = models.Q(Razdoblje_od__lte=self.Razdoblje_do, Razdoblje_do__gte=self.Razdoblje_do)
        # Queryset that finds all clashing timeslots with the same day
        queryset = self._meta.default_manager.filter(Razdoblje_od_in_range | Razdoblje_do_in_range)
        if self.pk:
            queryset = queryset.exclude(pk=self.pk) # Exclude this object if it is already saved to the database
        if queryset.exists():
            raise ValidationError('An existing timeslot clashes with the given one!') 

        super().clean(*args, **kwargs)

    


    
    @property
    def sazetak(self):
        return str(self)
