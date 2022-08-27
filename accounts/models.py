from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    age = models.IntegerField(null=True)
    #IntegerField→数字
    user = models.OneToOneField(User, related_name="userinfo", on_delete=models.CASCADE)
    # on_delete 片方消したら両方消えるようにする。
    username = models.CharField(null=True, max_length=30)