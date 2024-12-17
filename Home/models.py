from django.db import models
# Create your models here.

class user_model(models.Model):
    name=models.CharField(max_length=100, blank=True,null=True)
    email=models.EmailField(blank=True,null=True)  # Valeur par défaut
    password=models.CharField(max_length=100,blank=True,null=True)
    
    class Meta:
        verbose_name="user_model"
        verbose_name_plural = "user_models"