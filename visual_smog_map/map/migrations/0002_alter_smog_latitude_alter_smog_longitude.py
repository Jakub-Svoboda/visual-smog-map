# Generated by Django 4.2.3 on 2023-07-30 15:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smog',
            name='latitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)]),
        ),
        migrations.AlterField(
            model_name='smog',
            name='longitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)]),
        ),
    ]
