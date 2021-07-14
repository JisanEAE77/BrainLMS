from django.db import models
from student.models import ClassType, Subject
from django.contrib.auth.models import User
from tinymce import HTMLField

# Create your models here.


class SubscriptionType(models.Model):
    name = models.CharField(blank=False, max_length=100)
    slug = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.slug


class TutionSubscription(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, blank=False, null=False)
    subscription_type = models.OneToOneField(SubscriptionType, on_delete=models.CASCADE, blank=False, null=False)
    fee = models.BigIntegerField(blank=False, null=False)
    hpd = models.IntegerField(blank=False, null=False)
    description = HTMLField(max_length=100000, blank=False, null=False)
    classType = models.OneToOneField(ClassType, on_delete=models.CASCADE, blank=False, null=False)
    thumbnail = models.ImageField(upload_to='gig_thumbnail', blank=False, null=False)
    

    def __str__(self):
        return (self.subject + " - " + self.author + " (Class: " + self.classType + ", Duration: " + self.subscription_type + " )") 


class InstructorProfile(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    dp =  models.ImageField(upload_to='instructor_dp')
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, blank=False)


class TotalInstructor(models.Model):
    total = models.BigIntegerField()