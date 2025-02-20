# api/models.py

from django.contrib.gis.db import models
from datetime import datetime

class OceanCurrentData(models.Model):
    # Latitude et Longitude sous forme de point géographique
    location = models.PointField()
    
    # La date et l'heure associée
    timestamp = models.DateTimeField()
    
    # La valeur spécifique à chaque point (mlotst_mean)
    mlotst_mean = models.FloatField()

    def __str__(self):
        return f"Data for {self.timestamp} at {self.location} with mlotst_mean={self.mlotst_mean}"
