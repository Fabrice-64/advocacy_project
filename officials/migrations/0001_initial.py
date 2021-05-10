# Generated by Django 3.1.5 on 2021-05-09 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MandateInterCom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Date de Début de Mandat')),
                ('function', models.CharField(choices=[('CHAIR', 'Président'), ('VCHAIR', 'Vice-Président'), ('COUNS', 'Conseiller'), ('UNK', 'Non Renseigné')], default='UNK', max_length=6, verbose_name='Fonction Occupée')),
                ('intercom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.intercom')),
            ],
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=240, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=240, verbose_name='Nom')),
                ('influence_level', models.CharField(choices=[('0-INF', 'Aucune influence'), ('1-INF', "Peu d'influence"), ('2-INF', 'Influence moyenne'), ('3-INF', 'Influence élevée'), ('4-INF', 'Influence très élevée')], default='2-INF', max_length=5, verbose_name='Influence')),
                ('propinquity_level', models.CharField(choices=[('0-PROPINQ', 'Idées incompatibles'), ('1-PROPINQ', 'Idées presque compatibles'), ('2-PROPINQ', 'Idées compatibles'), ('3-PROPINQ', 'Idées proches'), ('4-PROPINQ', 'Mêmes idées'), ('UNK-PROPINQ', 'Idées inconnues')], default='UNK-PROPINQ', max_length=11, verbose_name='proximité')),
                ('attached_volunteer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.volunteer', verbose_name='Bénévole dédié')),
                ('intercoms', models.ManyToManyField(through='officials.MandateInterCom', to='communities.Intercom')),
            ],
        ),
        migrations.CreateModel(
            name='NationalMandate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Date de Début de Mandat')),
                ('function', models.CharField(choices=[('MP', 'Député'), ('SEN', 'Sénateur'), ('UNK', 'Non Renseigné')], default='UNK', max_length=6, verbose_name='Mandat National')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.department')),
                ('official', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officials.official')),
            ],
        ),
        migrations.CreateModel(
            name='MandateRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Date de Début de Mandat')),
                ('function', models.CharField(choices=[('CHAIR', 'Président'), ('VCHAIR', 'Vice-Président'), ('COUNS', 'Conseiller'), ('UNK', 'Non Renseigné')], default='UNK', max_length=6, verbose_name='Fonction Occupée')),
                ('official', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officials.official')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.region')),
            ],
        ),
        migrations.AddField(
            model_name='mandateintercom',
            name='official',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officials.official'),
        ),
        migrations.CreateModel(
            name='MandateDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Date de Début de Mandat')),
                ('function', models.CharField(choices=[('CHAIR', 'Président'), ('VCHAIR', 'Vice-Président'), ('COUNS', 'Conseiller'), ('UNK', 'Non Renseigné')], default='UNK', max_length=6, verbose_name='Fonction Occupée')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.department')),
                ('official', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officials.official')),
            ],
        ),
        migrations.CreateModel(
            name='MandateCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Date de Début de Mandat')),
                ('function', models.CharField(choices=[('CHAIR', 'Président'), ('VCHAIR', 'Vice-Président'), ('COUNS', 'Conseiller'), ('UNK', 'Non Renseigné')], default='UNK', max_length=6, verbose_name='Fonction Occupée')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.city')),
                ('official', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officials.official')),
            ],
        ),
    ]
