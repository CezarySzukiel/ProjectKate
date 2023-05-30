from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from exercises_app.models import Exercises
# Create your models here.


class UserSettings(models.Model):
    """User settings model.
    One to one relation with User model,
    level - True if user have advanced math skills"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    exercises = models.ManyToManyField(Exercises, blank=True)

    def __str__(self):
        return self.user.username

