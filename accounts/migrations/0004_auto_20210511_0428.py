# Generated by Django 3.1.5 on 2021-05-11 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20210510_0613'),
        ('accounts', '0003_auto_20210510_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.team', verbose_name='Equipe'),
        ),
    ]