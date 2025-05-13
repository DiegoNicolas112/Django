from django.db import models

# Create your models here.
class Manufacturers(models.Model):
    name = models.CharField(max_length=30)
    country_origin = models.CharField(max_length=30)
    date_of_fundation = models.DateField()
    website = models.URLField()

    # Esto es la representación dentro de Django
    def __str__(self):
        return self.name

class Smartphone(models.Model):
    manufacturers = models.ForeignKey(Manufacturers, on_delete=models.CASCADE) # CASCADE al borrar manufacturers también elimina los Smartphone.
    name = models.CharField(max_length=30)
    ram = models.IntegerField()
    storage = models.IntegerField()
    screen_size = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} ({self.manufacturers.name})"