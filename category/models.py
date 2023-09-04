from django.db import models

# Create your models here.

class Category(models.Model):
    Category = models.TextField(max_length=50)