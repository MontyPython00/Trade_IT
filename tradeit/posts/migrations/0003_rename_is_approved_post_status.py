# Generated by Django 4.2 on 2024-11-11 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_post_created_post_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_approved',
            new_name='status',
        ),
    ]
