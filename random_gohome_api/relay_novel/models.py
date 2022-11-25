from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class relay_novel(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    def __str__(self):
        return self.title