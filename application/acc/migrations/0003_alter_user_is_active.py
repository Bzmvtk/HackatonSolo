# Generated by Django 4.0 on 2021-12-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
