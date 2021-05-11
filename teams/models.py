from django.db import models
from communities.models import City


# Create your models here.
class Team(models.Model):

    name = models.CharField("Nom d'Equipe", max_length=40, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Ville", null=True, blank=True)

    def __str__(self):
        return self.name