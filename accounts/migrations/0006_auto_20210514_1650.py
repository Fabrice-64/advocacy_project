# Generated by Django 3.1.5 on 2021-05-14 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20210511_0428'),
        ('accounts', '0005_auto_20210512_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='teams.team', verbose_name='Equipe'),
        ),
    ]
