from django.db import models
from django.contrib.auth.models import User

class number(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
