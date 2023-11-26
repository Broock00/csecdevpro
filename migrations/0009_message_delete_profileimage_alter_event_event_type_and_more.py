# Generated by Django 4.2.2 on 2023-11-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Club_MMS', '0008_alter_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=255)),
                ('sender_email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('reply', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfileImage',
        ),
        migrations.AlterField(
            model_name='event',
            name='Event_type',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Conference', 'Conference'), ('Workshop', 'Workshop'), ('Hackathons', 'Hackathons'), ('TechTalks', 'TechTalks'), ('Project_Showcases', 'Project_Showcases'), ('Coding Competitions', 'Coding Competitions'), ('Collaborative Projects', 'Collaborative Projects'), ('Charity Events', 'Charity Events')], default='-------', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='Image',
            field=models.ImageField(upload_to='staticfiles/media/'),
        ),
    ]