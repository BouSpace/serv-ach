from http import client
from django import views
from django.urls import path
from . import views

urlpatterns = [

    #------- Lien API Client ----------
    path('clients/',views.allClients),
    path('client/<int:id>/',views.getclient),
    path('addclients/',views.addClient),
    path('updclient/<int:id>/',views.updClient),
    path('deleteclient/<int:id>/',views.delClient),

    #------- Lien API Article ----------
    path('articles/',views.allArticles),
    path('article/<int:id>/',views.getArticle),
    path('addarticle/',views.addArticle),
    path('updarticle/<int:id>/',views.updArticle),
    path('deletearticle/<int:id>/',views.delArticle),
    
]
