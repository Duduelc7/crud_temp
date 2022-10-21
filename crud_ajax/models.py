from msilib.schema import ListView
from unicodedata import name
from django.db import models

# Create your models here.


class Conta(models.Model):
    id = models.BigAutoField(primary_key=True)
    desc = models.CharField(max_length=200,verbose_name='Descrição')
    fornecedor = models.CharField(max_length=255)