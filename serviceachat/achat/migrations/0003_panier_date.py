# Generated by Django 4.1.2 on 2022-10-31 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achat', '0002_remove_panier_date_ligneachat_article_panier_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='panier',
            name='date',
            field=models.DateField(default='2022-01-01'),
        ),
    ]
