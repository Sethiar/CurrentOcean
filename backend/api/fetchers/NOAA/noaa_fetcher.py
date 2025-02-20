""" 
Requête viant à récupérer les données des courants océaniques
depuis le site NOAA 

"""

import os
import requests

from django.shortcuts import render

from dotenv import load_dotenv


# Chargement des variables d'environnement
load_dotenv()

def fetch_noaa_data(request):
    """
    Fonction pour récupérer les données des courants marins depuis l'API NOAA
    et les afficher dans la vue.
    """
    #Chargement du token de NOAA dpuis .env
    NOAA_TOKEN = os.getenv('NOAA_TOKEN')

    #URL de l'API NOAA pour récupérer les données
    NOAA_API_URL = "https://www.ncdc.noaa.gov/cdo-web/api/datasets"

    headers = {
        'token': NOAA_TOKEN
    }

    # Effectuer la requête pour récupérer les données
    response = requests.get(NOAA_API_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Traitement de données, enregistrement dans la base de données.
        for item in data['results']:
            # Enregistrement / mise àjour des données.
            Current.objects.update_or_create(
                name=item['name'],
                defaults={
                    'ocean': item.get('ocean', 'Indéfini'),
                    'speed': item.get('speed', 0),
                    'temperature' : item.get('temperature', 0),
                    'salinity': item.get('salinity', 0),
                    'force': item.get('force', 0),
                    'direction': item.get('direction', 'Indéfini'),
                    'depth': item.get('depth', 0)
                }
        )
        
        # Afficher les courants marins récupérés
        return render(request, 'core/current_list.html', {'currents': Current.objects.all()})
    else:
        return render(request, 'core/error.html', {'error': 'Erreur lors de la visuallisation des données.'})
    
    