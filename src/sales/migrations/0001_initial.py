# Generated by Django 5.1.3 on 2024-11-20 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateField(verbose_name='Date de vente')),
                ('product', models.CharField(max_length=30, verbose_name='Produit')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Client')),
            ],
        ),
    ]
