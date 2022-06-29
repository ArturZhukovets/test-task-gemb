from django.db import models

# Create your models here.
class Restaurant_infoModel(models.Model):
    name = models.CharField(max_length=120)
    supervisor = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['supervisor']