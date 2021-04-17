from django.db import models
from accounts.models import Volunteer
import communities.models as comms
# Create your models here.
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
                    on_delete=models.CASCADE,
                    verbose_name="Bénévole dédié",
                    blank=True)
    intercoms = models.ManyToManyField(comms.Intercom,
                            through='MandateIntercom')

class MandateInterCom(models.Model):
    class MandateLevel(models.TextChoices):
        CHAIR =  "CHAIR", "Président"
        VICE_CHAIR = "VCHAIR", "Vice-Président"
        COUNSELLOR = "COUNS", "Conseiller"
        UNK = "UNK", "Non Renseigné"
    verbose_name="Mandat Intercommunal"
    official = models.ForeignKey(Official,
            on_delete=models.CASCADE)
    intercom = models.ForeignKey(comms.Intercom, 
            on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="Date de Début de Mandat")
    function = models.CharField(max_length=6,
                            blank=False,
                            null=False,
                            default=MandateLevel.UNK,
                            choices=MandateLevel.choices,
                            verbose_name="Fonction Occupée")

class MandateCity(models.Model):
    class MandateLevel(models.TextChoices):
        CHAIR =  "CHAIR", "Président"
        VICE_CHAIR = "VCHAIR", "Vice-Président"
        COUNSELLOR = "COUNS", "Conseiller"
        UNK = "UNK", "Non Renseigné"
    verbose_name="Mandat Municipal"
    official = models.ForeignKey(Official,
            on_delete=models.CASCADE)
    city = models.ForeignKey(comms.City, 
            on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="Date de Début de Mandat")
    function = models.CharField(max_length=6,
                            blank=False,
                            null=False,
                            default=MandateLevel.UNK,
                            choices=MandateLevel.choices,
                            verbose_name="Fonction Occupée")

class MandateDepartment(models.Model):
    class MandateLevel(models.TextChoices):
        CHAIR =  "CHAIR", "Président"
        VICE_CHAIR = "VCHAIR", "Vice-Président"
        COUNSELLOR = "COUNS", "Conseiller"
        UNK = "UNK", "Non Renseigné"
    verbose_name="Mandat Conseil Départemental"
    official = models.ForeignKey(Official,
            on_delete=models.CASCADE)
    department = models.ForeignKey(comms.Department, 
            on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="Date de Début de Mandat")
    function = models.CharField(max_length=6,
                            blank=False,
                            null=False,
                            default=MandateLevel.UNK,
                            choices=MandateLevel.choices,
                            verbose_name="Fonction Occupée")

class MandateRegion(models.Model):
    class MandateLevel(models.TextChoices):
        CHAIR =  "CHAIR", "Président"
        VICE_CHAIR = "VCHAIR", "Vice-Président"
        COUNSELLOR = "COUNS", "Conseiller"
        UNK = "UNK", "Non Renseigné"
    verbose_name="Mandat Conseil Régional"
    official = models.ForeignKey(Official,
            on_delete=models.CASCADE)
    region = models.ForeignKey(comms.Region, 
            on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="Date de Début de Mandat")
    function = models.CharField(max_length=6,
                            blank=False,
                            null=False,
                            default=MandateLevel.UNK,
                            choices=MandateLevel.choices,
                            verbose_name="Fonction Occupée")


class NationalMandate(models.Model):
    class MandateType(models.TextChoices):
       MP = "MP", "Député"
       SEN = "SEN", "Sénateur"
       UNK = "UNK",, "Non Renseigné"
    official = models.ForeignKey(Official,
            on_delete=models.CASCADE)
    department = models.ForeignKey(comms.Department, 
            on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="Date de Début de Mandat")
    function = models.CharField(max_length=6,
                            blank=False,
                            null=False,
                            default=MandateType.UNK,
                            choices=MandateType.choices,
                            verbose_name="Mandat National")