from django.db import models

# Create your models here.
class main_page(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created_at= models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(
        upload_to= 'images/', blank = True
        )
    def __str__(self):
        return self.title
    
class comment(models.Model):
    article = models.ForeignKey(main_page, on_delete=models.CASCADE, related_name = 'comments')
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content