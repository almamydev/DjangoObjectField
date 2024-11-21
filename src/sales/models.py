from django.db import models


class Sale(models.Model):
    sale_date = models.DateField(verbose_name="Date de vente")
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, verbose_name="Client")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name="Produit")

    def __str__(self):
        return f"{self.sale_date.strftime('%d-%m%-%Y')} | {self.client.fullname} | {self.product}"
    
