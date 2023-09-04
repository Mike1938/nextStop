from django.db import models
from places.models import Places

# Create your models here.
class Links(models.Model):
    link = models.URLField(max_length=200)
    place = models.ForeignKey(Places, default=None, on_delete=models.CASCADE)
