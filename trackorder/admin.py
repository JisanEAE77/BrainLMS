from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(OrderStatus)
admin.site.register(GigOrder)
admin.site.register(TutionSubscriptionOrder)