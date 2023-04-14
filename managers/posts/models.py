from django.db import models

class PostManager(models.Manager):
    def sorted(self):
        return self.get_queryset().order_by('-created_at')



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = PostManager()

    def __str__(self):
        return self.title