from dataclasses import fields
from rest_framework import serializers
from .models import Client, Article, Panier, LigneAchat

class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

"""
class lignAchatSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = LigneAchat
        fields = '__all__'

class panierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panier
        fields = '__all__'
"""
class lignAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneAchat
        fields = ['id','prixUnitaire','quantite']

class panierSerializer(serializers.ModelSerializer):
    paniers = lignAchatSerializer(many=True, read_only=True)

    class Meta:
        model = Panier
        fields = ["id",'date','reference','statut','paniers']
