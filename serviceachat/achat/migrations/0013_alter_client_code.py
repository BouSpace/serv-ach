# Generated by Django 4.1.3 on 2022-11-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achat', '0012_client_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.CharField(max_length=25, unique=True, verbose_name='Code'),
        ),
    ]
