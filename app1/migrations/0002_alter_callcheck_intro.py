# Generated by Django 4.1.3 on 2022-11-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callcheck',
            name='intro',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
