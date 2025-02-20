import xarray as xr
import pandas as pd

import os

chemin_fichier = "../copernicus-data/copernicus_data_22_23.nc"

def lire_fichier_nc(chemin_fichier):
    print(f"📊 Tentative de lecture du fichier : {chemin_fichier}")
    
    try:
        ds = xr.open_dataset(chemin_fichier)
        print("📂 Contenu du fichier chargé avec succès !")
        print(ds)  # Affiche les métadonnées du fichier
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier : {e}")

def main():
    fichier_test = "../copernicus-data/copernicus_data_22_23.nc"

    if not os.path.exists(fichier_test):
        print(f"❌ Le fichier {fichier_test} est introuvable !")
    else:
        print(f"✅ Le fichier {fichier_test} existe bien.")
        lire_fichier_nc(fichier_test)

if __name__ == "__main__":
    main()
