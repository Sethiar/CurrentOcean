from rest_framework.response import Response
from rest_framework.views import APIView
from api.fetchers.GDP.gdp_fetcher import fetch_gdp_data

class GDPDataView(APIView):
    def get(self, request):
        data = fetch_gdp_data()
        return Response(data)