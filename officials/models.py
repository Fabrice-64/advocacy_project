import uuid
from django.db import models
from accounts.models import Volunteer
import communities.models as comms
# Create your models here.

YEAR_CHOICE = [(f"{year}", f"{year}") for year in range(1975, 2030)]


class Official(models.Model):
    class InfluenceLevel(models.TextChoices):
            INFLUENCE_0 = "0-INF", "Aucune influence"
            INFLUENCE_1 = "1-INF", "Peu d'influence"
            INFLUENCE_2 = "2-INF", "Influence moyenne"
            INFLUENCE_3 = "3-INF", "Influence élevée"
            INFLUENCE_4 = "4-INF", "Influence très élevée"
    
    class PropinquityLevel(models.TextChoices):
            PROPINQ_0 = "0-PROPINQ", "Idées incompatibles"
            PROPINQ_1 = "1-PROPINQ", "Idées presque compatibles"
            PROPINQ_2 = "2-PROPINQ", "Idées compatibles"
            PROPINQ_3 = "3-PROPINQ", "Idées proches"
            PROPINQ_4 = "4-PROPINQ", "Mêmes idées"
            PROPINQ_UNK = "UNK-PROPINQ", "Idées inconnues"
    
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)

    first_name = models.CharField(max_length=240,
                    verbose_name="Prénom")
    last_name = models.CharField(max_length=240,
                    verbose_name="Nom")
    influence_level = models.CharField(max_length=5,
                            choices=InfluenceLevel.choices,
                            default=InfluenceLevel.INFLUENCE_2,
                            verbose_name="Influence")
    propinquity_level = models.CharField(max_length=11,
                            choices=PropinquityLevel.choices,
                            default=PropinquityLevel.PROPINQ_UNK,
                            verbose_name="proximité")
    attached_volunteer = models.ForeignKey(Volunteer,
                    on_delete=models.DO_NOTHING,
                    verbose_name="Bénévole dédié",
                    blank=True, null=True)
    mandate_intercom = models.ManyToManyField('MandateIntercom', blank=True)
    mandate_city = models.ManyToManyField('MandateCity', blank=True)
    mandate_department = models.ManyToManyField('MandateDepartment', blank=True)
    mandate_region = models.ManyToManyField('MandateRegion', blank=True)
    mp_mandate = models.ManyToManyField('MPMandate', blank=True)
    senator_mandate = models.ManyToManyField('SenatorMandate', blank=True)

    def __str__(self):
            return self.first_name + " " + self.last_name


class MandateInterCom(models.Model):
    class MandateLevel(models.TextChoices):
            CHAIR =  "CHAIR", "Président"
            VICE_CHAIR = "VCHAIR", "Vice-Président"
            COUNSELLOR = "COUNS", "Conseiller"
            UNK = "UNK", "Non Renseigné"
    verbose_name="Mandat Intercommunal"
    intercom = models.ForeignKey(comms.Intercom, 
            on_delete=models.CASCADE)
    start_year = models.CharField(verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)
    function = models.CharField(max_length=6,
                            blank=False,
                            null=False,
                            default=MandateLevel.UNK,
                            choices=MandateLevel.choices,
                            verbose_name="Fonction Occupée")
    
    def __str__(self):
            return self.function + " " + self.intercom.name + " " + str(self.start_year)


class MandateCity(models.Model):
    class MandateLevel(models.TextChoices):
            MAYOR =  "MAIRE", "Maire"
            DEPUTY = "ADJOINT", "Adjoint au Maire"
            COUNSELLOR = "COUNS", "Conseiller Municipal"
            UNK = "UNK", "Non Renseigné"
    verbose_name="Mandat Municipal"
    city = models.ForeignKey(comms.City, 
            on_delete=models.CASCADE)
    start_year = models.CharField(verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)
    function = models.CharField(max_length=7,
                            blank=False,
                            null=False,
                            default=MandateLevel.UNK,
                            choices=MandateLevel.choices,
                            verbose_name="Fonction Occupée")
    
    def __str__(self):
            return self.function + " " + self.city.name + " " + str(self.start_year)


class MandateDepartment(models.Model):
    class MandateLevel(models.TextChoices):
            CHAIR =  "Président", "Président"
            VICE_CHAIR = "Vice-Président", "Vice-Président"
            COUNSELLOR = "Conseiller", "Conseiller"
            UNK = "UNK", "Non Renseigné"
    verbose_name="Mandat Conseil Départemental"
    department = models.ForeignKey(comms.Department, 
            on_delete=models.CASCADE)
    start_year = models.CharField(verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)
    function = models.CharField(max_length=14,
                            blank=False,
                            null=False,
                            default=MandateLevel.UNK,
                            choices=MandateLevel.choices,
                            verbose_name="Fonction Occupée")
    def __str__(self):
            return self.function + " " + self.department.name + " " + str(self.start_year)


class MandateRegion(models.Model):
    class MandateLevel(models.TextChoices):
            CHAIR =  "CHAIR", "Président"
            VICE_CHAIR = "VCHAIR", "Vice-Président"
            COUNSELLOR = "COUNS", "Conseiller"
            UNK = "UNK", "Non Renseigné"
    verbose_name="Mandat Conseil Régional"
    region = models.ForeignKey(comms.Region, 
            on_delete=models.CASCADE)
    start_year = models.CharField(verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)
    function = models.CharField(max_length=6,
                            blank=False,
                            null=False,
                            default=MandateLevel.UNK,
                            choices=MandateLevel.choices,
                            verbose_name="Fonction Occupée")

    def __str__(self):
            return self.function + " " + self.region.name + " " + str(self.start_year)

class MPMandate(models.Model):
    department = models.ForeignKey(comms.Department, 
            on_delete=models.CASCADE)
    start_year = models.CharField(verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)

    def __str__(self):
            return self.department.name + " " + str(self.start_year)

class SenatorMandate(models.Model):
    department = models.ForeignKey(comms.Department, 
            verbose_name="Département",
            on_delete=models.CASCADE,
            related_name="senator_mandate")
    start_year = models.CharField(verbose_name="Année de Début de Mandat",
        max_length=4,
        choices=YEAR_CHOICE)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['department', 'start_year'], name='unique_mandate_department')]

    def __str__(self):
            return self.department.name + " " + str(self.start_year)