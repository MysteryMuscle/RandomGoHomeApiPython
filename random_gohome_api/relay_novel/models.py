from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class relay_novel(models.Model):
    """
        relay novel model
    """
    id = models.AutoField(primary_key=True)

    # if prev novel is deleted, then this novel will be deleted
    prev = models.ForeignKey('self', related_name="prev_novel", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=False)
    image = models.CharField(max_length=1000, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)

    is_first = True if prev is None else False
    is_last = True if next is None else False
    
    is_ended = models.BooleanField(default=False)

    def reply(self, content, author, image=None, url=None):
        if self.is_ended:
            raise Exception("This novel is ended")
        else:
            new_novel = relay_novel(prev=self, title=self.title, author=author, content=content, image=image, url=url)
            new_novel.save()
            return new_novel

    def replyByRequest(self, request):
        """
            reply novel
        """
        user = User.objects.get(id=request.data['author'])
        new_novel = self.reply(
            request.data['content'],
            user,
            request.data['image'],
            request.data['url']
        )
        return new_novel

    def __str__(self):
        return self.title