# Generated by Django 4.2.2 on 2023-11-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Club_MMS', '0007_alter_event_date_and_time_alter_event_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]
