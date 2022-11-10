# Generated by Django 4.1.3 on 2022-11-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achat', '0006_ligneachat_panier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='intitule',
            field=models.CharField(max_length=100, verbose_name='Intitule'),
        ),
        migrations.AlterField(
            model_name='article',
            name='prix',
            field=models.FloatField(default=0, verbose_name='Prix de vente'),
        ),
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.CharField(max_length=25, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(max_length=25, verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='ligneachat',
            name='quantite',
            field=models.IntegerField(default=0, verbose_name='Quantite'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='reference',
            field=models.CharField(max_length=20, unique=True, verbose_name='Reference'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='statut',
            field=models.BooleanField(default=False, verbose_name='Statut du panier'),
        ),
    ]
