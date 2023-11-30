from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class Event(models.Model):
    EVENT_TYPES = [
        ('Seminar', 'Seminar'),('Conference', 'Conference'),('Workshop', 'Workshop'),
        ('Hackathons', 'Hackathons'),('TechTalks', 'TechTalks'),('Project_Showcases', 'Project_Showcases'),
        ('Coding Competitions', 'Coding Competitions'),('Collaborative Projects', 'Collaborative Projects'),('Charity Events', 'Charity Events'),
    ]
    Event_name = models.CharField(max_length=100)
    Event_type = models.CharField(max_length=50, choices=EVENT_TYPES,default='-------')
    Description = models.TextField(blank = True,max_length=100000)
    Date_and_Time= models.CharField(max_length=100) 
    Location = models.CharField(max_length=100)
    Organizer = models.CharField(blank = True,max_length=100)
    Capacity = models.PositiveIntegerField()
    Today = models.DateTimeField(default=timezone.now)
    Image = models.ImageField(blank = True,upload_to = "staticfiles/media/")

    def __str__(self):
        return self.Event_name


class CustomUser(AbstractUser):
    FIELD_CHOICES = [
    ("CE", "Civil Engineering"),
    ("AR", "Architect"),
    ("CSE", "Computer Science and Engineering"),
    ("SE", "Software Engineering"),
    ("ECE", "Electronics and Communication Engineering"),
    ("EPC", "Electrical Power and Control Engineering"),
    ("ME", "Mechanical Engineering"),
    ("CH", "Chemical Engineering"),
    ("MSE", "Material Science and Engineering"),
    ]

    User_ID = models.CharField(max_length=20,blank=True)
    Phone_number = models.CharField(max_length=13, blank=True)
    Gender = models.CharField(max_length=1, blank=True, choices=[('M', 'Male'), ('F', 'Female')])
    Department = models.CharField(max_length=50, blank=True, choices = FIELD_CHOICES)



class SpecialAnnouncement(models.Model):
    date_time = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title