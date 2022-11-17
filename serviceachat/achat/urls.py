import email
from http import client
from django import views
from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Mater 2022-2023 - Service Web TP',
        default_version='1.0.0',
        description="Service achat en ligne\n\n**TEAM  **\n*BOUSSIM Issa*\n*GANAME Ali*\n*NACOULMA Judion*\n*SAKANDE Odile*\n*SORO Adam*",
        terms_of_service='https://bianlu.pythonanywhere.com/api/clients/',
        contact=openapi.Contact(email=""),
        license=openapi.License(name="School License"),
        
    ),
    public=True,
#    permission_classes=(permissions.AllowAny,)
)

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
    path('addarticles/',views.addArticle),
    path('updarticle/<int:id>/',views.updArticle),
    path('deletearticle/<int:id>/',views.delArticle),

    #------- Lien API Panier ----------
    path('paniers/',views.allClientPanier),
    path('panier/<int:id>/',views.getPanier),
    path('addpaniers/',views.addPanier),
    path('deletepanier/<int:id>/',views.delPanier),
    path('addachat/',views.addLigneAchat),
    path('achatClient/',views.allLigneAchat),
    path('delarticleachat/<int:panier_id>/<int:article_id>/',views.delLigneAchat),

    #path('updpanier/<int:id>/',views.updArticle),
    #path('validepanier/<int:id>/',views.panierValide),


    #path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #path('',schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('swagger',schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
    #path('login/',views.login),
]
