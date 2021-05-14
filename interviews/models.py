from django.db import models
from django.urls import reverse
from accounts.models import Volunteer, CustomUser
from officials.models import Official
from datetime import date

# Create your models here.
class AdvocacyTopic(models.Model):
    is_active = models.BooleanField(verbose_name="Thème actif", null=True)
    keyword = models.CharField(verbose_name="Mot-Clé", max_length=20, null=True, blank=True)
    key_statement = models.CharField(max_length=240, 
                                    blank=False, 
                                    null=False,
                                    verbose_name="Phrase Clé")
    slug = models.SlugField(max_length=250, unique_for_date='creation_date', null=True)
    source_title = models.CharField(max_length=140, null=True, blank=True, verbose_name="Titre de la Source")
    source = models.URLField(max_length=240,
                            blank=True,
                            verbose_name="Lien vers la source")
    quote = models.CharField(max_length=480,
                            blank=True, null=True, verbose_name="Citation")
    creation_date = models.DateField(auto_now_add=True, verbose_name="Date de Création")
    updated_date = models.DateField(auto_now=True, verbose_name="Date de Mise à Jour")
    created_by = models.ForeignKey(CustomUser, models.SET_NULL, null=True, blank=True, verbose_name="Rédacteur")

    def get_absolute_url(self):
        return reverse('interviews:advocacy_topic_detail', args=[str(self.slug)])

    def __str__(self):
        return self.key_statement

class Interview(models.Model):
    class InterviewStatus(models.Model):
        PENDING = 'PDG' 
        XED = 'XED'
        DONE = 'DON'
        ITW_STATUS = [
            (PENDING, "Interview Prévue"),
            (XED, "Interview Annulée"),
            (DONE, "Interview Réalisée"),
        ]      
    
    class InterviewAssessment(models.Model):
        GOAL_100_PC = "100PC"
        GOAL_75_PC = "75PC"
        GOAL_50_PC = "50PC"
        GOAL_25_PC = "25PC"
        GOAL_0_PC = "0PC"
        TBD = "TBD"
        ITW_ASSESS = [
            (GOAL_100_PC, "Objectif Totalement Atteint"),
            (GOAL_75_PC, "Objectif Largement Atteint"),
            (GOAL_50_PC, "Objectif à Moitié Atteint"),
            (GOAL_25_PC, "Atteinte limitée de l'Objectif"),
            (GOAL_0_PC, "Echec de l'Entretien"),
            (TBD, "Non Renseigné"),
        ]


    date_planned = models.DateField(verbose_name="Date prévue")
    date_effective = models.DateField(verbose_name="Date de réalisation")
    status = models.CharField(max_length=3,
                            blank=False,
                            null=False,
                            default=InterviewStatus.PENDING,
                            choices=InterviewStatus.ITW_STATUS,
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
                            choices=InterviewAssessment.ITW_ASSESS,
                            verbose_name="Evaluation de l'entretien")
    comments = models.CharField(max_length=420,
                                blank=True,
                                null=False,
                                default="Non Renseigné",
                                verbose_name="Commentaires")
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    official = models.ForeignKey(Official, on_delete=models.CASCADE)
    topics = models.ManyToManyField(AdvocacyTopic)
