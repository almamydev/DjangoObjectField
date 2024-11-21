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

    @classmethod
    def filter_by_name(cls, name: str, queryset: models.QuerySet) -> list["Client"]:
        name_parts = name.split(" ")
        filtered_clients = []
        for client in queryset:
            for name_part in name_parts:
                if name_part.strip() and name_part.lower() in client.fullname().lower():
                    filtered_clients.append(client)
                    break
        return filtered_clients