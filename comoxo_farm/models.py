from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta

STATUS = ((0, "Inactive"), (1, "Active"))
HORTICULTURE = ((0, "Fruit"), (1, "Vegetable"), (2, "Flower"), (3, "Others"))

class EditableField(models.Model):
    field_id = models.CharField(max_length=255)
    field_title = models.CharField(max_length=255, default='title')
    field_content = models.TextField()
    field_img = models.ImageField(upload_to='assets',default='default.jpg')

    def __str__(self):
        return self.field_id

def return_date_time_now():
    now = timezone.now()
    return now

def return_date_time():
    now = timezone.now()
    return now + timedelta(days=90)

class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='tasks',default='default_task.jpg')
    start_date = models.DateTimeField(default=return_date_time_now)
    end_date = models.DateTimeField(default=return_date_time)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.title

class Team(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    content = models.TextField()
    pic = models.ImageField(upload_to='team', default='default_post.jpg')

    def __str__(self):
        return self.title

class Crop(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField(choices=HORTICULTURE, default=0)
    def __str__(self):
        return self.name