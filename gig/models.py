from django.db import models
from student.models import ClassType, Subject
from django.contrib.auth.models import User
from tinymce import HTMLField

# Create your models here.


class TutionGig(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, blank=False)
    pph = models.BigIntegerField(blank=False)
    description = HTMLField(max_length=100000, blank=False)
    classType = models.OneToOneField(ClassType, on_delete=models.CASCADE, blank=False)
    thumbnail = models.ImageField(upload_to='gig_thumbnail', blank=False)

    def __str__(self):
        return (self.subject + " - " + self.author + " (Class: " + self.classType + ")") 
    