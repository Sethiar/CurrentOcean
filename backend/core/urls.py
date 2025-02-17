from django.urls import path
from .views import ocean_currents , index

urlpatterns = [
    path('currents/', ocean_currents, name='currents_list'),
    path("", index, name="index"),
]
