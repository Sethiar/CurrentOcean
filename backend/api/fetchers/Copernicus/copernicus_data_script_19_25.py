
import os
from datetime import datetime, timedelta
import copernicusmarine
from dotenv import load_dotenv

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()


def fetch_copernicus_data_19_25(start_date, end_date, output_directory="copernicus-data"):
    """
    Récupère les données Copernicus pour un intervalle de temps donné et les enregistre dans un fichier NetCDF.

    Cette fonction effectue une requête à l'API Copernicus Marine pour récupérer des données sur les courants marins,
    les températures de la surface de la mer, la salinité, etc., entre deux dates spécifiées.

    Arguments :
    - start_date (datetime) : La date de début de la période pour récupérer les données.
    - end_date (datetime) : La date de fin de la période pour récupérer les données.
    - output_directory (str) : Le répertoire où les données seront sauvegardées. Par défaut "copernicus-data".

    Retour :
    - data (dict) : Les données récupérées, retournées par la fonction `copernicusmarine.subset`.
    """

    # Identifiants Copernicus Marine
    username = os.getenv('COPERNICUS_USERNAME')
    password = os.getenv('COPERNICUS_PASSWORD')

    # Parmaètres de la requête
    dataset_id="dataset-armor-3d-nrt-monthly"
    variables=["so", "to", "ugo", "vgo"]

  
    longitude_range = (-179.875, 179.875)
    latitude_range = (-80, 90)
    depth = (0, 10)
    
    # Format des dates compatible avec l'API
    start_datetime = start_date.strftime("%Y-%m-%dT%H:%M:%S")
    end_datetime = end_date.strftime("%Y-%m-%dT%H:%M:%S")
    
    # Demander les données via l'API Copernicus Marine
    output_filename = f"copernicus_data_{start_date.year}_{start_date.month:02d}.nc"  # Nom dynamique du fichier
    data = copernicusmarine.subset(
        dataset_id=dataset_id,
        variables=variables,
        minimum_longitude=longitude_range[0],
        maximum_longitude=longitude_range[1],
        minimum_latitude=latitude_range[0],
        maximum_latitude=latitude_range[1],
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        minimum_depth=depth[0],
        maximum_depth=depth[1],
        output_filename=output_filename,  # Fichier de sortie
        output_directory=output_directory,  # Dossier de sortie
        username=username,
        password=password
    )

    # Vérifier si le fichier a été créé et renvoyer un message
    file_path = os.path.join(output_directory, output_filename)
    if os.path.exists(file_path):
        print(f"Fichier pour {start_date.strftime('%B %Y')} téléchargé avec succès.")
    else:
        print(f"Le fichier pour {start_date.strftime('%B %Y')} n'a pas été téléchargé.")

    return data


def automate_data_requests():
    """
    Automatise la récupération des données Copernicus sur la période donnée.

    Cette fonction itère sur chaque mois de la période spécifiée et appelle `fetch_copernicus_data_XX` pour récupérer les
    données de chaque mois. Les données sont sauvegardées dans le répertoire spécifié avec un nom de fichier unique par mois.

    Elle est appelée de manière automatique pour récupérer toutes les données de la période souhaitée.
    """
    # Date de début et de fin de la période à récupérer
    start_date = datetime(2019, 1, 1)
    end_date = datetime(2025, 12, 1)

    current_date = start_date

    # Boucle sur chaque mois entre start_date et end_date
    while current_date < end_date:
        # Calculer la date de fin du mois actuel
        next_month = current_date + timedelta(days=32)
        next_month = next_month.replace(day=1)  # Passer au mois suivant

        # Appeler la fonction pour récupérer les données pour le mois courant
        fetch_copernicus_data_19_25(current_date, next_month)

        # Passer au mois suivant
        current_date = next_month