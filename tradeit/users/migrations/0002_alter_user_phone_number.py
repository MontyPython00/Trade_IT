# Generated by Django 4.2 on 2024-10-15 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=9, unique=True, validators=[django.core.validators.MinLengthValidator(9)]),
        ),
    ]
