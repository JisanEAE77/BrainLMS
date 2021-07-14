from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClassType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    dp =  models.ImageField(upload_to='student_dp')
    classStandard = models.OneToOneField(ClassType, on_delete=models.CASCADE)


class TotalStudent(models.Model):
    total = models.BigIntegerField()