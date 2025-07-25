from django.db import models

# Create your models here.

class Basemodel(models.Model):

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)


class EventModel(Basemodel):

    name = models.CharField(max_length=150)
    place = models.CharField(max_length=100)
    phno = models.CharField(max_length=10)