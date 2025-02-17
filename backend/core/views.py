import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse

from core.models import Current  # Import depuis core

# Vue qui va permettre de servir la page home du site currentocean
def index(request):
    return redirect("http://localhost:5173/")


def ocean_currents(request):
    currents = Current.objects.all()
    return render(request, 'core/current.html', {'currents': currents})


