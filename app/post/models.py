from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  head = models.CharField(max_length = 256)
  text = models.TextField()
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.head
