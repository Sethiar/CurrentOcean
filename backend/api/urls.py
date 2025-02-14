from django.urls import path, include
from .views.views import CurrentListAPIView
from api.views.gdp_views import GDPDataView

urlpatterns = [
    path('currents/', CurrentListAPIView.as_view(), name='api-current-list'),
    path('gdp-data/', GDPDataView.as_view(), name='gdp_data'),
    path('blog/', include('blog.urls')),
]
