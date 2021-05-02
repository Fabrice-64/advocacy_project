from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .teams import Teams
from django.contrib.auth.models import Group

# Create your models here.
class CustomUser(AbstractUser):

    class StatusType(models.Model):
        VOLUNTEER = "VOLUNTEER"
        MANAGER = "MANAGER"
        EMPLOYEE = "EMPLOYEE"
        STATUS = [
            (MANAGER, "Manager"),
            (EMPLOYEE, "Employé"),
            (VOLUNTEER, "Bénévole"),
        ]
   
    status_type = models.CharField(
        max_length=50,
        choices=StatusType.STATUS, 
        default=StatusType.VOLUNTEER,
        verbose_name="Statut")

    id = models.BigAutoField(primary_key=True)
    phone_regex = RegexValidator(
        regex=r"^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$",
        message="Veuillez entrer un numéro valide"
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length = 14,
        blank = True,
        help_text="Veuillez entrer un numéro Français",
        verbose_name="Téléphone"
    )

    team = models.CharField(
        max_length=4,
        choices=Teams.choices,
        default=Teams.STRASBOURG_VILLE,
        verbose_name="Equipe"
    )

class VolunteerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(status_type=CustomUser.StatusType.VOLUNTEER)

class ManagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(status_type=CustomUser.StatusType.MANAGER)

class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(status_type=CustomUser.StatusType.EMPLOYEE)


class Volunteer(CustomUser):
    objects = VolunteerManager()

    class Meta:
        proxy = True
        ordering = ["team", "last_name"]
        

class Employee(CustomUser):
    objects = EmployeeManager()

    class Meta:
        proxy = True


class Manager(CustomUser):
    objects = ManagerManager()
    
    class Meta:
        proxy = True