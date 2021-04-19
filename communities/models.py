from django.db import models
from django_oso.models import AuthorizedModel
# Create your models here.
class Region(AuthorizedModel):
    name = models.CharField(verbose_name="Région",
                            max_length=240)

class Department(models.Model):
    name = models.CharField(verbose_name="Département",
                            max_length=240)
    dept_number = models.CharField(verbose_name="numéro de département",
                                   max_length=3)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                            verbose_name="Région")

class Intercom(models.Model):
    name = models.CharField(max_length=240,
                            verbose_name="Intercommunalité")

class City(models.Model):
    name = models.CharField(max_length=240,
                            verbose_name="Ville")
    department = models.ForeignKey(Department,
                                on_delete=models.CASCADE,
                                verbose_name="Département")
    intercom = models.ForeignKey(Intercom,
                        on_delete=models.CASCADE,
                        verbose_name="Intercommunalité")