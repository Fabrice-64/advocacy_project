# Generated by Django 3.1.5 on 2021-04-27 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0006_auto_20210425_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='department',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, to='communities.department', verbose_name='Département'),
        ),
        migrations.AlterField(
            model_name='intercom',
            name='department',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='communities.department', verbose_name='Département'),
        ),
    ]