from django.urls import path, include
from api.views.gdp_views import GDPDataView
from api.views.noaa_views import fetch_noaa_data_view

urlpatterns = [
    path('fetch-noaa-data/', fetch_noaa_data_view, name='fetch-noaa-data'),
    path('gdp-data/', GDPDataView.as_view(), name='gdp_data'),
    path('blog/', include('blog.urls')),
]
