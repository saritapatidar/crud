from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=100)
    stufathername=models.CharField(max_length=200)
    num=models.IntegerField()
