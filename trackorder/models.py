from django.db import models
from gig.models import TutionGig
from instructor.models import TutionSubscription

# Create your models here.

class OrderStatus(models.Model):
    status = models.CharField(max_length=100, blank=False)

class GigOrder(models.Model):
    gig = models.OneToOneField(TutionGig, on_delete=models.CASCADE, blank=False)
    order_status = models.OneToOneField(OrderStatus, on_delete=models.CASCADE, blank=False)

class TutionSubscriptionOrder(models.Model):
    subscription = models.OneToOneField(TutionSubscription, on_delete=models.CASCADE)
    order_status = models.OneToOneField(OrderStatus, on_delete=models.CASCADE, blank=False)