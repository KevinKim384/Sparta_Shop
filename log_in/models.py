from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class login_manage(models.Model):
    id = models.TextField(primary_key=True)
    password = models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add = True) # add는 생성때 추가
    updated_at = models.DateTimeField(auto_now = True)
    
class User(AbstractUser):
    pass