# Generated by Django 4.1.2 on 2022-11-02 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achat', '0005_panier_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ligneachat',
            name='panier',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='achat.client'),
        ),
    ]
