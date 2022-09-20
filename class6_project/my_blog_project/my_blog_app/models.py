from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from datetime import datetime

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date_created = models.DateTimeField(default= timezone.now)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Post Object: {self.title} by {self.owner}'