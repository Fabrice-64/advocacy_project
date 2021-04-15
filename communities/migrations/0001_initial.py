# Generated by Django 3.1.5 on 2021-04-14 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intercom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Intercommunalité')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Région')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Département')),
                ('dept_number', models.CharField(max_length=3, verbose_name='numéro de département')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.region', verbose_name='Région')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Ville')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.department', verbose_name='Département')),
                ('intercom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.intercom', verbose_name='Intercommunalité')),
            ],
        ),
    ]