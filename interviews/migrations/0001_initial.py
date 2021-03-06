# Generated by Django 3.1.5 on 2021-05-22 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('officials', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvocacyTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(null=True, verbose_name='Thème actif')),
                ('keyword', models.CharField(blank=True, choices=[('Emploi', 'Emploi'), ('Formation', 'Formation'), ('Migrations', 'Migrations'), ('Logement', 'Logement'), ('Ecologie', 'Ecologie'), ('Pauvreté', 'Pauvreté')], default=None, max_length=20, null=True, verbose_name='Mot-Clé')),
                ('key_statement', models.CharField(max_length=240, verbose_name='Phrase Clé')),
                ('slug', models.SlugField(max_length=250, null=True, unique_for_date='creation_date')),
                ('source_title', models.CharField(blank=True, max_length=140, null=True, verbose_name='Titre de la Source')),
                ('source', models.URLField(blank=True, max_length=240, verbose_name='Lien vers la source')),
                ('quote', models.TextField(blank=True, max_length=600, null=True, verbose_name='Citation')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='Date de Mise à Jour')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Rédacteur')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_planned', models.DateField(blank=True, null=True, verbose_name='Date prévue')),
                ('date_effective', models.DateField(blank=True, null=True, verbose_name='Date de réalisation')),
                ('status', models.CharField(choices=[('1-PDG', 'Interview Prévue'), ('0-XED', 'Interview Annulée'), ('2-DON', 'Interview Réalisée'), ('3-COM', 'Interview Réalisée et Evaluée')], default='1-PDG', max_length=5, verbose_name="Statut de l'interview")),
                ('goal', models.CharField(max_length=420, verbose_name='Objectif')),
                ('outcome', models.CharField(blank=True, max_length=420, null=True, verbose_name='Résultats')),
                ('assessment', models.CharField(choices=[('100PC', 'Objectif Totalement Atteint'), ('75PC', 'Objectif Largement Atteint'), ('50PC', 'Objectif à Moitié Atteint'), ('25PC', "Atteinte limitée de l'Objectif"), ('0PC', "Echec de l'Entretien"), ('TBD', 'Non Renseigné')], default='TBD', max_length=5, verbose_name="Evaluation de l'entretien")),
                ('comments', models.CharField(blank=True, max_length=420, verbose_name='Commentaires')),
                ('official', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officials.official', verbose_name='Elu')),
                ('topics', models.ManyToManyField(blank=True, to='interviews.AdvocacyTopic', verbose_name='Thèmes')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.volunteer', verbose_name='Bénévole')),
            ],
        ),
    ]
