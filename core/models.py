from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Country_data(models.Model):
    country= models.CharField(max_length=255)
    population= models.DecimalField(decimal_places=1,max_digits=8)
   
    def __str__(self):
        return str(self.country)

    @property
    def num_likes(self):
        return self.liked.all().count()

