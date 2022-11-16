from lib2to3.pgen2.token import tok_name
from symbol import sym_name
import this
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    s_name = models.CharField(null=True, max_length=30)
    t_name = models.CharField(null=True, max_length=30)
    
    def __str__(self):
        return self.s_name
    
class TimeTable(models.Model):
    mon1 = models.ForeignKey(Subject, verbose_name="月1", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    mon2 = models.ForeignKey(Subject, verbose_name="月2", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    mon3 = models.ForeignKey(Subject, verbose_name="月3", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    mon4 = models.ForeignKey(Subject, verbose_name="月4", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    mon5 = models.ForeignKey(Subject, verbose_name="月5", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    mon6 = models.ForeignKey(Subject, verbose_name="月6", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    tue1 = models.ForeignKey(Subject, verbose_name="火1", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    tue2 = models.ForeignKey(Subject, verbose_name="火2", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    tue3 = models.ForeignKey(Subject, verbose_name="火3", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    tue4 = models.ForeignKey(Subject, verbose_name="火4", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    tue5 = models.ForeignKey(Subject, verbose_name="火5", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    tue6 = models.ForeignKey(Subject, verbose_name="火6", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    wed1 = models.ForeignKey(Subject, verbose_name="水1", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    wed2 = models.ForeignKey(Subject, verbose_name="水2", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    wed3 = models.ForeignKey(Subject, verbose_name="水3", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    wed4 = models.ForeignKey(Subject, verbose_name="水4", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    wed5 = models.ForeignKey(Subject, verbose_name="水5", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    wed6 = models.ForeignKey(Subject, verbose_name="水6", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    thu1 = models.ForeignKey(Subject, verbose_name="木1", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    thu2 = models.ForeignKey(Subject, verbose_name="木2", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    thu3 = models.ForeignKey(Subject, verbose_name="木3", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    thu4 = models.ForeignKey(Subject, verbose_name="木4", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    thu5 = models.ForeignKey(Subject, verbose_name="木5", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    thu6 = models.ForeignKey(Subject, verbose_name="木6", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    fri1 = models.ForeignKey(Subject, verbose_name="金1", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    fri2 = models.ForeignKey(Subject, verbose_name="金2", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    fri3 = models.ForeignKey(Subject, verbose_name="金3", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    fri4 = models.ForeignKey(Subject, verbose_name="金4", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    fri5 = models.ForeignKey(Subject, verbose_name="金5", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    fri6 = models.ForeignKey(Subject, verbose_name="金6", on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    
class Person(models.Model):
    age = models.IntegerField(null=True)
    #IntegerField→数字
    user = models.OneToOneField(User, related_name="userinfo", on_delete=models.CASCADE, unique=True)
    # on_delete 片方消したら両方消えるようにする。
    username = models.CharField(null=True, max_length=30)
    # アイコン画像
    icon = models.ImageField(upload_to='media/icon_images', blank=True, null=True)
    timetable = models.OneToOneField(TimeTable, verbose_name="時間割", on_delete=models.CASCADE, null=True, blank=True)