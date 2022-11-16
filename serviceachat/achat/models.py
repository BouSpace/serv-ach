from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Client(models.Model):
    code = models.CharField('Code',max_length=25,unique=True)
    nom = models.CharField('Client',max_length=25)
    telephone = models.CharField('Telephone',max_length=18,null=True)

    def __str__(self) -> str:
        return '%s %s' % (self.code, self.nom)

class Article(models.Model):
    intitule = models.CharField('Intitule',max_length=100)
    description = models.TextField('Description',null=True)
    prix = models.FloatField('Prix de vente',default=0)

    def __str__(self) -> str:
        return '{} {}'.format(self.intitule,self.prix)

class Panier(models.Model):
    date = models.DateField('Date',auto_now=True)
    reference = models.CharField('Reference',max_length=20,unique=True)
    statut = models.BooleanField('Statut du panier',default=False)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING,default=1)

class LigneAchat(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING,default=1)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE,default=1,related_name='panier')
    prixUnitaire = models.FloatField('Prix unitaire',default=0)
    quantite = models.IntegerField('Quantite',default=0)
    