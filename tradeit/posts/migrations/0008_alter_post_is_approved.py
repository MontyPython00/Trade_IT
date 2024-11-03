# Generated by Django 4.2 on 2024-11-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_approved',
            field=models.IntegerField(choices=[(2, 'Pending'), (1, 'Approved'), (0, 'Denied')], default=2),
        ),
    ]
