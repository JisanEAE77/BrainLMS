from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TutionSubscription)
admin.site.register(SubscriptionType)
admin.site.register(InstructorProfile)
admin.site.register(TotalInstructor)