# import uuid 
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
from django.urls import reverse
from django_countries.fields import CountryField 
# Create your models here.
class Trip(models.Model):
    '''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )'''
    name = models.CharField(max_length=200)
    country = CountryField(max_length=200)
    destination = CountryField(max_length=200)
    start = models.DateField(default=datetime.now)
    end = models.DateField(default=datetime.now) 
    activity = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('travel_detail', args=[str(self.id)])
