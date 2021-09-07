from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    CHOICES = (
        ('poem', 'POEM'),
        ('article', 'ARTICLE'),
        ('yarn', 'YARN'),
    )

    title = models.CharField(max_length=150)
    content = models.TextField()
    section = models.CharField(max_length=100, choices=CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.title

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comment_author', on_delete=models.CASCADE)
    opinion = models.TextField()

    def __unicode__(self):
        return self.opinion
