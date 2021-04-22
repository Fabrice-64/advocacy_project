from django.db import models
from django_oso.models import AuthorizedModel
# Create your models here.
class Region(AuthorizedModel):
    name = models.CharField(verbose_name="Région",
                            max_length=240,
                            unique=True)
    def __str__(self):
        return self.name 

class Department(models.Model):
    name = models.CharField(verbose_name="Département",
                            max_length=240,
                            unique=True)
    dept_number = models.CharField(verbose_name="numéro de département",
                                   max_length=3,
                                   unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                            verbose_name="Région")
    def __str__(self):
        return self.name 

class Intercom(models.Model):
    name = models.CharField(max_length=240,
                            verbose_name="Intercommunalité")
    department = models.ForeignKey(Department,
                                on_delete=models.CASCADE,
                                verbose_name="Département",
                                default="14")
    def __str__(self):
        return self.name 

class City(models.Model):
    name = models.CharField(max_length=240,
                            verbose_name="Ville")
    department = models.ForeignKey(Department,
                                on_delete=models.CASCADE,
                                verbose_name="Département",
                                default="14")
    intercom = models.ForeignKey(Intercom,
                        on_delete=models.CASCADE,
                        verbose_name="Intercommunalité",
                        default="4")
    def __str__(self):
        return self.name 