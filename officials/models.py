"""
    The model Official and the various Mandate models are developped in this module.
    The French territorial organization is closely linked to the departments. Therefore,
    almost every mandate is attached to a department: even a senator is elected as a department
    representative.

"""
import uuid
from django.db import models
from django.urls import reverse
from accounts.models import Volunteer
import communities.models as comms
# Create your models here.

YEAR_CHOICE = [(f"{year}", f"{year}") for year in range(1975, 2030)]


class Official(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    first_name = models.CharField(
        max_length=240,
        verbose_name="Prénom")
    last_name = models.CharField(
        max_length=240,
        verbose_name="Nom")
    attached_volunteer = models.ForeignKey(
        Volunteer,
        on_delete=models.DO_NOTHING,
        verbose_name="Bénévole dédié",
        blank=True, null=True)
    mandate_intercom = models.ManyToManyField(
        'MandateIntercom', blank=True,
        verbose_name="Mandats Intercommunaux")
    mandate_city = models.ManyToManyField(
        'MandateCity', blank=True,
        verbose_name="Mandats Municipaux")
    mandate_department = models.ManyToManyField(
        'MandateDepartment', blank=True,
        verbose_name="Mandat de Conseiller Départemental")
    mandate_region = models.ManyToManyField(
        'MandateRegion', blank=True,
        verbose_name="Mandat de Conseiller Régional")
    mp_mandate = models.ManyToManyField(
        'MPMandate', blank=True,
        verbose_name="Mandat de Député")
    senator_mandate = models.ManyToManyField(
        'SenatorMandate', blank=True,
        verbose_name="Mandat de Sénateur")

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('officials:official_details', args=[str(self.id)])


class MandateInterCom(models.Model):
    class MandateLevel(models.TextChoices):
        CHAIR = "CHAIR", "Président"
        VICE_CHAIR = "VCHAIR", "Vice-Président"
        COUNSELLOR = "COUNS", "Conseiller"
        UNK = "UNK", "Non Renseigné"
    verbose_name = "Mandat Intercommunal"
    intercom = models.ForeignKey(
        comms.Intercom,
        on_delete=models.CASCADE,
        verbose_name="Intercommunalité",
        null=True, blank=True)
    department = models.ForeignKey(
        comms.Department,
        on_delete=models.CASCADE,
        verbose_name="Département",
        null=True, blank=True)
    start_year = models.CharField(
        verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)
    function = models.CharField(
        max_length=6,
        blank=False,
        null=False,
        default=MandateLevel.UNK,
        choices=MandateLevel.choices,
        verbose_name="Fonction Occupée")

    def __str__(self):
        return self.get_function_display() + " " + self.intercom.name + " " + str(self.start_year)


class MandateCity(models.Model):
    class MandateLevel(models.TextChoices):
        MAYOR = "MAIRE", "Maire"
        DEPUTY = "ADJOINT", "Adjoint au Maire"
        COUNSELLOR = "COUNS", "Conseiller Municipal"
        UNK = "UNK", "Non Renseigné"
    verbose_name = "Mandat Municipal"
    city = models.ForeignKey(
        comms.City,
        on_delete=models.CASCADE,
        verbose_name="Commune",
        null=True, blank=True)
    intercom = models.ForeignKey(
        comms.Intercom,
        on_delete=models.CASCADE,
        verbose_name="Intercommunalité",
        null=True, blank=True)
    department = models.ForeignKey(
        comms.Department,
        on_delete=models.CASCADE,
        verbose_name="Département",
        null=True, blank=True)
    start_year = models.CharField(
        verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)
    function = models.CharField(
        max_length=7,
        blank=False,
        null=False,
        default=MandateLevel.UNK,
        choices=MandateLevel.choices,
        verbose_name="Fonction Occupée")

    def __str__(self):
        return self.get_function_display() + " " + self.city.name + " " + str(self.start_year)


class MandateDepartment(models.Model):
    class MandateLevel(models.TextChoices):
        CHAIR = "Président", "Président"
        VICE_CHAIR = "Vice-Président", "Vice-Président"
        COUNSELLOR = "Conseiller", "Conseiller"
        UNK = "UNK", "Non Renseigné"
    verbose_name = "Mandat Conseil Départemental"
    department = models.ForeignKey(
        comms.Department,
        on_delete=models.CASCADE,
        verbose_name="Département",
        null=True, blank=True)
    start_year = models.CharField(
        verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)
    function = models.CharField(
        max_length=14,
        blank=False,
        null=False,
        default=MandateLevel.UNK,
        choices=MandateLevel.choices,
        verbose_name="Fonction Occupée")

    def __str__(self):
        return self.get_function_display() + " " + self.department.name + " " + str(self.start_year)


class MandateRegion(models.Model):
    class MandateLevel(models.TextChoices):
        CHAIR = "CHAIR", "Président"
        VICE_CHAIR = "VCHAIR", "Vice-Président"
        COUNSELLOR = "COUNS", "Conseiller"
        UNK = "UNK", "Non Renseigné"
    verbose_name = "Mandat Conseil Régional"
    region = models.ForeignKey(
        comms.Region,
        on_delete=models.CASCADE,
        null=True, blank=True)
    start_year = models.CharField(
        verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)
    function = models.CharField(
        max_length=6,
        blank=False,
        null=False,
        default=MandateLevel.UNK,
        choices=MandateLevel.choices,
        verbose_name="Fonction Occupée")

    def __str__(self):
        return self.get_function_display() + " " + self.region.name + " " + str(self.start_year)


class MPMandate(models.Model):
    department = models.ForeignKey(
        comms.Department,
        on_delete=models.CASCADE,
        null=True, blank=True)
    start_year = models.CharField(
        verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)

    def __str__(self):
        return self.department.name + " " + str(self.start_year)


class SenatorMandate(models.Model):
    department = models.ForeignKey(
        comms.Department,
        verbose_name="Département",
        on_delete=models.CASCADE,
        related_name="senator_mandate",
        null=True, blank=True)
    start_year = models.CharField(
        verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['department', 'start_year'], name='unique_mandate_department')]

    def __str__(self):
        return self.department.name + " " + str(self.start_year)
