from django.db import models

class Teams(models.TextChoices):
    STRASBOURG_VILLE = "STB1", "Strasbourg-Ville"
    STRASBOURG_NEUHOF = "STBN", "Strasbourg-Neuhof"
    MULHOUSE_CENTRE = "MLHC", "Mulhouse-Centre"
    HAGUENAU = "HGN", "Haguenau"
