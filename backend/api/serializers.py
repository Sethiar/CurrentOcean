"""
Fichier qui transforme les objets Dlango en JSON
"""

from rest_framework import serializers
from core.models import Current

class CurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Current
        fields = '__all__'  # Inclusion de tous les champs du modèle