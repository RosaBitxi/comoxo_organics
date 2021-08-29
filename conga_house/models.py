from django.db import models
from users.models import CustomUser

STATUS = ((0, "Available"), (1, "Occupied"),(2, "Maintenance"))

class EditableField_Conga(models.Model):
    field_id = models.CharField(max_length=255)
    field_title = models.CharField(max_length=255, default='title')
    field_content = models.TextField()
    field_img = models.ImageField(upload_to='assets',default='default.jpg')

    def __str__(self):
        return self.field_id

class Room(models.Model):
    name = models.CharField(max_length=255, default="Bedroom")
    desc = models.CharField(max_length=255, default="Blank")
    floor = models.IntegerField(default=0)
    roomsq = models.IntegerField(default=19)
    status = models.IntegerField(choices=STATUS, default=1)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="conga_tenant")
    pic = models.ImageField(default='default.jpg',upload_to='rooms')

    def __str__(self):
        return self.name