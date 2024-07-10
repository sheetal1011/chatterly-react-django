from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=250)
    description=models.TextField()
    image_path=models.CharField(max_length=255,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    #updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Comments(models.Model):
    blog=models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    text=models.CharField(max_length=250)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text