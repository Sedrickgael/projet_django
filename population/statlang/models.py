from django.db import models
from django.db.models import Sum

# Create your models here.

class Population(models.Model):
    """Model definition for Population."""

    nom = models.CharField(max_length=255)
    nb_hbts = models.PositiveIntegerField(default=0)
    

    class Meta:
        """Meta definition for Population."""

        verbose_name = 'Population'
        verbose_name_plural = 'Populations'

    @property
    def pourcentage(self):
        somme= Population.objects.all().aggregate(som=Sum('nb_hbts'))
        proportion=(self.nb_hbts / somme['som'])*100
        return round(proportion, 2)
    
    def __str__(self):
        """Unicode representation of Population."""
        return '{}'.format(self.nom ) # TODO
