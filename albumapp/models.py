from django.db import models
from django.forms import widgets

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural="Categories"
        
    def __str__(self):
        return self.name
        
class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,default="Select")
    image = models.ImageField(upload_to="myphotos")
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.category)
    