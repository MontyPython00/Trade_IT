# Generated by Django 4.2 on 2024-10-15 20:34

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(6)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('category', models.CharField(choices=[('cars', 'Cars'), ('electronics', 'Electronics'), ('cards', 'Cards'), ('clothes', 'Clothes'), ('others', 'Others')], max_length=16)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
