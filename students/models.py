from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(default="",max_length=100)
    admno=models.CharField(default="",max_length=100)
    rollno=models.CharField(default="",max_length=100)
    college=models.CharField(default="",max_length=100)


