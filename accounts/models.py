from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .teams import Teams

# Create your models here.
class CustomUser(AbstractUser):
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
