# Generated by Django 3.0.5 on 2020-09-24 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyca', '0002_auto_20200911_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='course',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='specialisation',
            new_name='department',
        ),
    ]
