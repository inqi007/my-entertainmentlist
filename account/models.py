from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favorites(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usernames", default=0)
    name = models.CharField(max_length=256)

class Towatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", default=0)
    title = models.CharField(max_length=256)
