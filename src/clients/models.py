from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Prénom")
    last_name = models.CharField(max_length=30, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=30, verbose_name="Téléphone")
    
    def __str__(self):
        return self.fullname()
    
    def fullname(self):
        return self.first_name + " " + self.last_name
