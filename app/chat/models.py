from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    name = models.CharField(max_length = 256)
    member = models.ManyToManyField(User)
    chat = models.TextField()

    def __str__(self):
        return self.name
