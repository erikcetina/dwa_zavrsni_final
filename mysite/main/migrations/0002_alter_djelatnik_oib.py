# Generated by Django 4.0.1 on 2022-08-24 14:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djelatnik',
            name='OIB',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(10000000000), django.core.validators.MaxValueValidator(99999999999)]),
        ),
    ]
