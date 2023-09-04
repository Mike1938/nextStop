from django.db import models
from datetime import date
from category.models import Category

# Create your models here.
class Places(models.Model):
    name = models.TextField(max_length=100)
    dateAdded = models.DateField(default=date.today)
    completed = models.DateField(blank=True, null=True)
    desc = models.TextField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



