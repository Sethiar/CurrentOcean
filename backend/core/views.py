import os

from rest_framework import generics
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse


# Vue qui va permettre de servir la page home du site currentocean
# Redirection de l'utilisateur vers le frontend React
def index(request):
    """
    Vue qui redirige l'utilisateur vers la page d'accueil de l'applicaiton React.
    """
    return redirect("http://localhost:5173/")
