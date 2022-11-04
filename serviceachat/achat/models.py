from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Client(models.Model):
    code = models.CharField('Code',max_length=25)
    nom = models.CharField('Client',max_length=25)

    def __str__(self) -> str:
        return '%s %s' % (self.code, self.nom)

class Article(models.Model):
    intitule = models.CharField('Intitule',max_length=100)
    description = models.TextField('Description',null=True)
    prix = models.FloatField('Prix de vente',default=0)

    def __str__(self) -> str:
        return '%s %s' %  (self.intitule,self.prix)

class Panier(models.Model):
    date = models.DateField('Date',auto_now=True)
    reference = models.CharField('Reference',max_length=20)
    statut = models.BooleanField('Statut du panier',default=False)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING,default=0)

class LigneAchat(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING,default=0)
    panier = models.ForeignKey(Client, on_delete=models.CASCADE,default=0)
    prixUnitaire = models.FloatField('Prix unitaire',default=0)
    quantite = models.IntegerField('Quantite',default=0)
    
