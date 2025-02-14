from django.db import models

# Classe qui permet d'enregistrer les informations des courants marins.
class Current(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ocean = models.CharField(max_length=50, choices=[
        ('Antartic', 'Antartique'),
        ('Arctic', 'Arctique'),
        ('Atlantic', 'Atlantique'),
        ('Indian', 'Indien'),
        ('Pacific', 'Pacifique'),
        
    ])
    speed = models.FloatField(help_text="Vitesse du courant en m/s")
    temperature = models.FloatField(help_text="Température de l'eau en degrès(°C)")
    salinity = models.FloatField(help_text="Salinité en PSU")
    force = models.FloatField(help_text="Force du courant (coeff)")
    direction = models.CharField(max_length=50, help_text="Direction du courant")
    depth = models.IntegerField(help_text="Profondeur du courant en mètres")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.ocean})"