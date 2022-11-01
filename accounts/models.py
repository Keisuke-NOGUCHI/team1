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
    mon1 = models.ForeignKey(Subject, verbose_name="月1", on_delete=models.CASCADE, related_name="+", null=True)
    mon2 = models.ForeignKey(Subject, verbose_name="月2", on_delete=models.CASCADE, related_name="+", null=True)
    mon3 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    mon4 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    mon5 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    mon6 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    tue1 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    tue2 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    tue3 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    tue4 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    tue5 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    tue6 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    wed1 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    wed2 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    wed4 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    wed5 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    wed6 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    thu1 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    thu2 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    thu3 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    thu4 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    thu5 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    thu6 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    fri1 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    fri2 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    fri3 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    fri4 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    fri5 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    fri6 = models.ForeignKey(Subject, verbose_name="科目名", on_delete=models.CASCADE, related_name="+", null=True)
    
class Person(models.Model):
    age = models.IntegerField(null=True)
    #IntegerField→数字
    user = models.OneToOneField(User, related_name="userinfo", on_delete=models.CASCADE, unique=True)
    # on_delete 片方消したら両方消えるようにする。
    username = models.CharField(null=True, max_length=30)
    # アイコン画像
    icon = models.ImageField(upload_to='media/icon_images', blank=True, null=True)
    timetable = models.OneToOneField(TimeTable, verbose_name="時間割", on_delete=models.CASCADE, null=True, blank=True)