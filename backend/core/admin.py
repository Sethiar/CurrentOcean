from django.contrib import admin
from .models import Current


# Classe de l'administrateur
class CurrentAdmin(admin.ModelAdmin):
    list_display = ('name', 'ocean', 'speed', 'temperature', 'salinity', 'force', 'direction', 'depth')
    search_fields = ('name', 'ocean')
    list_filter = ('ocean',)

admin.site.register(Current, CurrentAdmin)
