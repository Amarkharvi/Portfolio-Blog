# Generated by Django 3.1 on 2020-08-28 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200828_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='categories',
            new_name='category',
        ),
    ]
