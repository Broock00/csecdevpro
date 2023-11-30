# Generated by Django 4.2.2 on 2023-11-30 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Club_MMS', '0012_alter_event_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='DateTime',
        ),
        migrations.AddField(
            model_name='event',
            name='Today',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='Description',
            field=models.TextField(blank=True, max_length=100000),
        ),
        migrations.AlterField(
            model_name='event',
            name='Image',
            field=models.ImageField(blank=True, upload_to='staticfiles/media/'),
        ),
    ]
