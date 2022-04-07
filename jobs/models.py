from django.db import models

class Teste(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()