from http import client
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.contrib.auth import authenticate
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.authtoken.models import Token
#from rest_framework.decorators import api_view, permission_classes
#from rest_framework.permissions import AllowAny
#from rest_framework.status import (
#    HTTP_400_BAD_REQUEST,
#    HTTP_404_NOT_FOUND,
#    HTTP_200_OK
#)
from .serializers import clientSerializer, articleSerializer, panierSerializer, lignAchatSerializer, LigneAchat
from .models import Article, Client, LigneAchat, Panier

#@csrf_exempt
#@api_view(["POST"])
#@permission_classes((AllowAny,))
#def login(request):
#    username = request.data.get("username")
#    password = request.data.get("password")
#    if username is None or password is None:
#        return Response({'error': 'Please provide both username and password'},
#                        status=HTTP_400_BAD_REQUEST)
#    user = authenticate(username=username, password=password)
#    if not user:
#        return Response({'error': 'Invalid Credentials'},
#                        status=HTTP_404_NOT_FOUND)
#    token, _ = Token.objects.get_or_create(user=user)
#    return Response({'token': token.key},
#                    status=HTTP_200_OK)

    # Create your views here.

#------------------------------#
#     API GESTION DE CLIENT    #
#------------------------------#

@api_view(['POST'])
def addClient(request):
    serializer = clientSerializer(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Impossible d'ajouter ce client")
    

# -------------------------------
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
@api_view(['PUT'])
def updClient(request,id):
    client = Client.objects.get(id=id)
    serializer = clientSerializer(instance = client, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Erreur de mise a jour")
    

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
def listAchat(request):
    paniers = Panier.objects.prefetch_related('panier').all()
    serialization = lignAchatSerializer(paniers, many = True)
    return Response(serialization.data)

@api_view(['GET'])
def achlist(request):
    ligneAch = Panier.objects.prefetch_related('id')
    serialization = lignAchatSerializer(ligneAch,many=True)
    return Response(serialization.data)

@api_view(['GET'])
def allClientPanier(request):
    paniers = Panier.objects.all()
    serialization = panierSerializer(paniers,many=True)
    return Response(serialization.data)

#@api_view(['GET'])
#def allAchatPanier(request):
#    achpanier = LigneAchat.objects.prefetch_related().all()
#    serialization = (achpanier,many=True)
#    return Response(serialization.data)

# -------------------------------
@api_view(['GET'])
def getPanier(request,id):
    panier = Panier.objects.get(id=id)
    serializer = panierSerializer(panier)
    return Response(serializer.data)

# -------------------------------
@api_view(['GET'])
def getPanier1(request,client_id):
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
    if panier.statut==True:
        return Response('Impossible de supprimer un achat valide')
    else:
        panier.delete()
        return Response('Suppression effectuée avec succès !!')

#-----------------------------------#
#     API GESTION DE LIGNE ACHAT    #
#-----------------------------------#
@api_view(['GET'])
def allLigneAchat(request,panier_id):
    ligneAchats = LigneAchat.objects.filter(panier__id=panier_id)
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


