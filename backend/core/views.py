from django.shortcuts import render
from core.models import Current  # Import depuis core

def ocean_currents(request):
    currents = Current.objects.all()
    return render(request, 'core/current.html', {'currents': currents})
