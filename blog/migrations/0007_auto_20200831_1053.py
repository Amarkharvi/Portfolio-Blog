# Generated by Django 3.1 on 2020-08-31 05:23

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=20),
        ),
    ]