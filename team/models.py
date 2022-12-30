from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class team1(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='team/')
    author = models.ForeignKey(User, related_name='team_author', on_delete=models.CASCADE)



    def __str__(self):
        return self.title