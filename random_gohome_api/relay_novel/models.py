from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class relay_novel(models.Model):

    id = models.AutoField(primary_key=True)
    # if prev novel is deleted, then this novel will be deleted
    prev = models.ForeignKey('self', related_name="prev_novel", on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=False)
    image = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)

    is_first = True if prev is None else False
    is_last = True if next is None else False
    
    is_ended = models.BooleanField(default=False)

    def __str__(self):
        return self.title
