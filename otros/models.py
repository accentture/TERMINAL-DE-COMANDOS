from django.db import models
from django.dispatch import receiver

#user provided by django
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT)
    language = models.CharField(max_length = 255)



