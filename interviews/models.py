from django.db import models
from accounts.models import Volunteer
from officials.models import Official

# Create your models here.
class AdvocacyTopic(models.Model):
    key_statement = models.CharField(max_length=240, 
                                    blank=False, 
                                    null=False,
                                    verbose_name="Phrases Clé")
    source = models.URLField(max_length=240,
                            blank=True,
                            verbose_name="Lien vers la source")

class Interview(models.Model):
    class InterviewStatus(models.TextChoices):
        PENDING = 'PDG', "Interview Prévue"
        XED = 'XED', "Interview Annulée"
        DONE = 'DON', "Interview Réalisée"
    
    class InterviewAssessment(models.TextChoices):
        GOAL_100_PC = "100PC", "Objectif Totalement Atteint"
        GOAL_75_PC = "75PC", "Objectif Largement Atteint"
        GOAL_50_PC = "50PC", "Objectif à Moitié Atteint"
        GOAL_25_PC = "25PC", "Atteinte limitée de l'Objectif"
        GOAL_0_PC = "0PC", "Echec de l'Entretien"
        TBD = "TBD", "Non Renseigné"


    date_planned = models.DateField(verbose_name="Date prévue")
    date_effective = models.DateField(verbose_name="Date de réalisation")
    status = models.CharField(max_length=3,
                            blank=False,
                            null=False,
                            default=InterviewStatus.PENDING,
                            choices=InterviewStatus.choices,
                            verbose_name="Statut de l'interview")
    goal = models.CharField(max_length=420,
                            blank=False,
                            null=False,
                            verbose_name="Objectifs")
    outcome = models.CharField(max_length=420, 
                            verbose_name="Résultats",
                            default="Résultats de l'interview")
    assessment = models.CharField(max_length=5,
                            default=InterviewAssessment.TBD,
                            choices=InterviewAssessment.choices,
                            verbose_name="Evaluation de l'entretien")
    comments = models.CharField(max_length=420,
                                blank=True,
                                null=False,
                                default="Non Renseigné",
                                verbose_name="Commentaires")
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    official = models.ForeignKey(Official, on_delete=models.CASCADE)
    topics = models.ManyToManyField(AdvocacyTopic)
