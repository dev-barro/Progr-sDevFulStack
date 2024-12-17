from django.contrib import admin
from .models import user_model
# Register your models here.
# Adminusee_model permet d'afficher les users sous forme de colonnes
class Adminusee_model(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')
admin.site.register(user_model,Adminusee_model)
