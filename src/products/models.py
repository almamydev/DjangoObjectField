from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nom")
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix de vente")

    def __str__(self):
        return f"{self.name} - {self.sale_price}F"