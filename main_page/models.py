from django.db import models

# Create your models here.
class main_page(models.Model):
    title = models.TextField(primary_key=True)
    content = models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(
        upload_to= 'images/', blank = True
        )
    def __str__(self):
        return self.title