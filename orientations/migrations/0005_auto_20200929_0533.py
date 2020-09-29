# Generated by Django 3.0.5 on 2020-09-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orientations', '0004_orientation_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orientation',
            old_name='time',
            new_name='time_from',
        ),
        migrations.AddField(
            model_name='orientation',
            name='time_till',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
    ]
