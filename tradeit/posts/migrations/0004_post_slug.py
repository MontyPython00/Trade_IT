# Generated by Django 4.2 on 2024-11-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_uuid_post_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='test', max_length=256),
            preserve_default=False,
        ),
    ]