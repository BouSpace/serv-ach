from http import client
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import clientSerializer, articleSerializer, panierSerializer, lignAchatSerializer
from .models import Article, Client

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

