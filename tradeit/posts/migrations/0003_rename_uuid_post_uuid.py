# Generated by Django 4.2 on 2024-11-01 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='UUID',
            new_name='uuid',
        ),
    ]
