from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    classbooked = models.BooleanField(default=False)
    class_conducted = models.BooleanField(default=False)
    trail_class_timing = models.DateField(default=timezone.now)
    Rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=12)
    opinion = models.TextField(max_length=2000, default=None, null=True, blank=True)