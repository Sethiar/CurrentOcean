from django.http import JsonResponse
from api.fetchers.NOAA.noaa_fetcher import fetch_noaa_data

def fetch_noaa_data_view(request):
    try:
        # Appel de la fonction fetch_noaa_data pour récupérer les données
        data = fetch_noaa_data()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)