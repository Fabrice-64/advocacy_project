"""
    The User model is organized around 3 sorts of Users:

    - The Manager,
    - The Employee,
    - The Volunteer
    In the V1 the Employee has no specific role. The Manager
    and the Volunteer are given specifc permissions.

    The id fields uses the UUID in order to limit the vulnerability of this website.
"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator
from django.urls import reverse
from teams.models import Team


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

    class PositionType(models.Model):
        NON_EMPLOYED = "Non Salarié"
        MANAGER = "Manager"
        EMPLOYEE = "Coordonnateur"
        POSITION = [
            (NON_EMPLOYED, "Non Salarié"),
            (MANAGER, "Manager"),
            (EMPLOYEE, "Coordonnateur"),
        ]

    def get_absolute_url(self):
        return reverse('staff_details', args=[str(self.id)])

    def __str__(self):
        return self.first_name + " " + self.last_name

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    status_type = models.CharField(
        max_length=50,
        choices=StatusType.STATUS,
        default=StatusType.VOLUNTEER,
        verbose_name="Statut")

    position = models.CharField(
        max_length=20,
        choices=PositionType.POSITION,
        default=PositionType.NON_EMPLOYED,
        verbose_name="Position")

    # this Regex fits with the French phone numbers.
    phone_regex = RegexValidator(
        regex=r"^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$",
        message="Veuillez entrer un numéro valide"
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=14,
        blank=True,
        help_text="Veuillez entrer un numéro Français",
        verbose_name="Téléphone"
    )

    team = models.ForeignKey(
        Team,
        verbose_name="Equipe",
        on_delete=models.DO_NOTHING,
        null=True, blank=True)


class VolunteerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            status_type=CustomUser.StatusType.VOLUNTEER)


class ManagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            status_type=CustomUser.StatusType.MANAGER)


class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            status_type=CustomUser.StatusType.EMPLOYEE)


class Volunteer(CustomUser):
    objects = VolunteerManager()

    class Meta:
        proxy = True
        ordering = ["team", "last_name"]

    def get_absolute_url(self):
        return reverse('volunteer_details', args=[str(self.id)])


class Employee(CustomUser):
    objects = EmployeeManager()

    class Meta:
        proxy = True


class Manager(CustomUser):
    objects = ManagerManager()

    class Meta:
        proxy = True
