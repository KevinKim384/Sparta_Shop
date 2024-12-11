from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.TextField(primary_key=True)
    password = models.CharField(max_length=50)