from django.urls import path
from .views import ocean_currents  # On retire CurrentListAPIView

urlpatterns = [
    path('currents/', ocean_currents, name='currents_list'),
]
