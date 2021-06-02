"""
    These models are a simplified replica of the French territorial 
    organization. Communities with specific status are not considered.
    However the user can tweak the system and consider one or the other
    as a department or a region.
    The French territorial hierarchy is organized as such:
    Country -> Region -> Department -> Intercommunality -> City.
"""

from django.db import models


class Region(models.Model):
    name = models.CharField(verbose_name="Région",
                            max_length=240,
                            unique=True)
    class Meta:
        ordering = ["name"]

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
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name 

class Intercom(models.Model):
    name = models.CharField(max_length=240,
                            verbose_name="Intercommunalité")
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,
                                on_delete=models.CASCADE,
                                verbose_name="Département")
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name 

class City(models.Model):
    name = models.CharField(max_length=240,
                            verbose_name="Ville")
    region = models.ForeignKey(
            Region, on_delete=models.CASCADE,
            verbose_name="Région")
    department = models.ForeignKey(Department,
                                on_delete=models.CASCADE,
                                verbose_name="Département",
                                related_name="department_city")
    intercom = models.ForeignKey(Intercom,
                        on_delete=models.CASCADE,
                        verbose_name="Intercommunalité",
                        related_name="intercom_city")
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name 