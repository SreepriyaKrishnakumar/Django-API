from django.db import models


class BaseModel(models.Model):

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    

class ContactModel(BaseModel):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)


# Create your models here.
