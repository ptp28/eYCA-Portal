# Generated by Django 3.0.5 on 2020-09-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyca', '0003_auto_20200924_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_card_pic',
            field=models.FileField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
