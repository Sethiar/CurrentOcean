import requests

def fetch_gdp_data():
    """Récupère les données du Global Drifter Program via ERDDAP."""
    
    # URL correctement formée avec les paramètres intégrés
    url = ("https://erddap.aoml.noaa.gov/gdp/erddap/tabledap/OSMC_RealTime.json?"
           "time,latitude,longitude,sst,sss,platform_id&"
           "time>=2024-01-01T00:00:00Z")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Vérifie si le statut HTTP est OK (200)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Test de la fonction
data = fetch_gdp_data()
print(data)

