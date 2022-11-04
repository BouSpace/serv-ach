from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Client(models.Model):
    code = models.CharField(max_length=25)
    nom = models.CharField(max_length=25)

class Article(models.Model):
    intitule = models.CharField(max_length=100)
    description = models.TextField(null=True)
    prix = models.FloatField(default=0)

class Panier(models.Model):
    date = models.DateField(auto_now=True)
    reference = models.CharField(max_length=20)
    statut = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING,default=0)

class LigneAchat(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING,default=0)
    panier = models.ForeignKey(Client, on_delete=models.CASCADE,default=0)
    prixUnitaire = models.FloatField('Prix unitaire',default=0)
    quantite = models.IntegerField(default=0)
    
