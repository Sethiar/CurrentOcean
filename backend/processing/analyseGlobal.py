
"""
Méthode permettant d'automatiser la lecture des fichiers reçus via l'API de Copernicus.

"""

import os
import xarray as xr
import pandas as pd
from datetime import datetime

# Définir le répertoire contenant les fichiers .nc et le dossier de destination pour les CSV
NC_DIRECTORY = 'C:/Users/Lefet/DjangoProject/CurrentOcean/backend/api/fetchers/Copernicus/copernicus-data'
CSV_DIRECTORY = 'C:/Users/Lefet/DjangoProject/CurrentOcean/backend/processing/fichier_CSV'


# Créer le dossier fichier_CSV s'il n'existe pas
os.makedirs(CSV_DIRECTORY, exist_ok=True)


def process_variable(ds, var_name, file_name):
    """
    Extrait une variable spécifique d'un dataset NetCDF et la sauvegarde en CSV.
    
    Args:
        ds (xarray.Dataset): Dataset NetCSDf chargé.
        var_name (str): Nom de la variable à extraire.
        file_name (str): Nom du fichier NetCDF d'origine.
    """
    
    try:
        if var_name not in ds:
            print(f"Variable {var_name} non trouvée dans le fichier {file_name}")
            return
        
        print(f"Extraction de {var_name} depuis {file_name}...")
        
        # Extraire la variable et convertir en DataFrame
        df = ds[[var_name]].to_dataframe().reset_index()
        
        # Générer un fichier CSV unique pour chaque varaible
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_csv = os.path.join(CSV_DIRECTORY, f"{var_name}_{timestamp}.csv")
        
        # Sauvegarder en CSV
        df.to_csv(output_csv, index=False)
        print(f"Fichier {var_name} sauveagardé : {output_csv}")
        
    except Exception as e:
        print(f"Erreur lors de l'extraction de {var_name} dans {file_name} : {e}")    
        
def load_and_process_nc(file_path):
    """
    Charge un fichier NetCDF (.nc), extrait une variable spécifique, et la sauvegarde en CSV.

    Args:
        file_path (str): Le chemin absolu ou relatif du fichier NetCDF à traiter.

    Cette fonction :
    - Ouvre le fichier NetCDF avec xarray.
    - Extrait la variable 'mlotst_mean' pour la première valeur temporelle.
    - Convertit les données extraites en DataFrame pandas.
    - Sauvegarde les données sous forme de fichier CSV dans le répertoire de travail.
    
    Si une erreur survient lors du traitement du fichier, un message d'erreur sera affiché.
    """
    try:
        # Charger en mode "chunked" pour éviter l'explosion mémoire
        ds = xr.open_dataset(file_path, chunks={'time': 1})
        
        # Liste des variables disponibles (exclut les coordonnées standards)
        variables = [var for var in ds.data_vars]
        
        if not variables:
            print(f"Aucune variable exploitable dans {file_path}")
            return

        print(f"Variables trouvées dans {file_path} : {variables}")
        
        # Extraire chaque variable individuellement
        for var in variables:
            process_variable(ds, var, os.path.basename(file_path))

        # Fermer proprement le dataset
        ds.close()

    except Exception as e:
        print(f"❌ Erreur lors du traitement du fichier {file_path}: {e}")


def process_all_nc_files(NC_DIRECTORY):
    """
    Parcourt tous les fichiers .nc dans le répertoire donné et les traite.

    Args:
        directory (str): Le chemin absolu ou relatif du répertoire contenant les fichiers .nc à traiter.

    Cette fonction :
    - Liste tous les fichiers avec l'extension .nc dans le répertoire spécifié.
    - Appelle la fonction `load_and_process_nc` pour chaque fichier trouvé.
    - Si aucun fichier .nc n'est trouvé, un message informatif est affiché.
    """
    # Lister tous les fichiers .nc dans le répertoire
    nc_files = [f for f in os.listdir(NC_DIRECTORY) if f.endswith('.nc')]
    
    if not nc_files:
        print("🚫 Aucun fichier .nc trouvé.")
        return
    
    # Traitement de chaque fichier
    print(f"📂 Fichiers trouvés : {nc_files}")
    for file in nc_files:
        file_path = os.path.join(NC_DIRECTORY, file)
        load_and_process_nc(file_path)


# Exécuter le traitement
process_all_nc_files(NC_DIRECTORY)