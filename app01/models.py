from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/images',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anonymity = models.BooleanField(default=False, blank=True, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

    # ログインユーザが投稿者かどうかを判断する
    def is_owner(self, user):
        if self.user.id == user.id:
            return True
        return False

class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/comment',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anonymity = models.BooleanField(default=False, blank=True, null=True)

    def is_owner(self, user):
        if self.user.id == user.id:
            return True
        return False