# Generated by Django 3.0.5 on 2020-09-09 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orientations', '0003_auto_20200903_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500)),
                ('student', models.BooleanField(default=True)),
                ('course', models.CharField(max_length=100)),
                ('specialisation', models.CharField(max_length=100)),
                ('email_id', models.EmailField(blank=True, max_length=254)),
                ('orientation_rating', models.IntegerField()),
                ('other_comments', models.CharField(max_length=1000)),
                ('orientation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orientations.Orientation')),
            ],
        ),
    ]
