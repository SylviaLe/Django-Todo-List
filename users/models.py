from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField()
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
#add name, last name, username. and email = sign ip 