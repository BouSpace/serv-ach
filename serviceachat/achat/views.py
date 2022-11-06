from http import client
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import clientSerializer, articleSerializer, panierSerializer, lignAchatSerializer
from .models import Article, Client, LigneAchat, Panier

    # Create your views here.

#------------------------------#
#     API GESTION DE CLIENT    #
#------------------------------#
@api_view(['GET'])
def allClients(request):
    clients = Client.objects.all()
    serialization = clientSerializer(clients,many=True)
    return Response(serialization.data)

# -------------------------------
@api_view(['GET'])
def getclient(request,id):
    client = Client.objects.get(id=id)
    serializer = clientSerializer(client)
    return Response(serializer.data)

# -------------------------------
@api_view(['POST'])
def addClient(request):
    serializer = clientSerializer(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# -------------------------------
@api_view(['PUT'])
def updClient(request,id):
    client = Client.objects.get(id=id)
    serializer = clientSerializer(instance = client, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

 #-------------------------------
@api_view(['DELETE'])
def delClient(request,id):
    client = Client.objects.get(id=id)
    client.delete()
    return Response('Suppression effectuée avec succès !!')

#------------------------------#
#     API GESTION DE ARTICLE    #
#------------------------------#
@api_view(['GET'])
def allArticles(request):
    articles = Article.objects.all()
    serialization = articleSerializer(articles,many=True)
    return Response(serialization.data)

# -------------------------------
@api_view(['GET'])
def getArticle(request,id):
    article = Article.objects.get(id=id)
    serializer = articleSerializer(article)
    return Response(serializer.data)

# -------------------------------
@api_view(['POST'])
def addArticle(request):
    serializer = articleSerializer(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# -------------------------------
@api_view(['PUT'])
def updArticle(request,id):
    article = Article.objects.get(id=id)
    serializer = articleSerializer(instance = article, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
 #-------------------------------
@api_view(['DELETE'])
def delArticle(request,id):
    article = Article.objects.get(id=id)
    article.delete()
    return Response('Suppression effectuée avec succès !!')


#------------------------------#
#     API GESTION DE PANIER    #
#------------------------------#
@api_view(['GET'])
def allClientPanier(request):
    paniers = Panier.objects.all()
    serialization = panierSerializer(paniers,many=True)
    return Response(serialization.data)

# -------------------------------
@api_view(['GET'])
def getPanier(request,client_id):
    panier = Panier.objects.filter(client__id=client_id)
    serializer = panierSerializer(panier)
    return Response(serializer.data)

# -------------------------------
@api_view(['POST'])
def addPanier(request):
    serializer = panierSerializer(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# -------------------------------
@api_view(['PUT'])
def updPanier(request,id):
    panier = Panier.objects.get(id=id)
    serializer = panierSerializer(instance = panier, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
 #-------------------------------
@api_view(['DELETE'])
def delPanier(request,id):
    panier = Panier.objects.get(id=id)
    panier.delete()
    return Response('Suppression effectuée avec succès !!')

#-----------------------------------#
#     API GESTION DE LIGNE ACHAT    #
#-----------------------------------#
@api_view(['GET'])
def allLigneAchat(request,panier_id):
    ligneAchats = LigneAchat.objects.filter(Panier__id=panier_id)
    serialization = lignAchatSerializer(ligneAchats,many=True)
    return Response(serialization.data)

# -------------------------------
@api_view(['GET'])
def getLigneAchat(request,id):
    panier = Panier.objects.get(id=id)
    serializer = lignAchatSerializer(panier)
    return Response(serializer.data)

# -------------------------------
@api_view(['POST'])
def addLigneAchat(request):
    serializer = lignAchatSerializer(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# -------------------------------
@api_view(['PUT'])
def updLigneAchat(request,id):
    lignAchat = LigneAchat.objects.get(id=id)
    serializer = lignAchatSerializer(instance = lignAchat, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
 #-------------------------------
@api_view(['DELETE'])
def delLigneAchat(request,id):
    panier = Panier.objects.get(id=id)
    panier.delete()
    return Response('Suppression effectuée avec succès !!')
