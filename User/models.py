from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Post(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
