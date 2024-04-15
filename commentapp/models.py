from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    full_name = models.CharField(max_length=50,blank=True,null=True)
    
    text = RichTextField()

    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name