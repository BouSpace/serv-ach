from django.contrib import admin
from .models import Client, Article, Panier, LigneAchat

# Register your models here.
admin.site.register(Client)
admin.site.register(Article)
admin.site.register(Panier)
admin.site.register(LigneAchat)
