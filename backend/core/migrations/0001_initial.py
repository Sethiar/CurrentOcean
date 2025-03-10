# Generated by Django 5.1.6 on 2025-02-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('ocean', models.CharField(choices=[('Antartic', 'Antartique'), ('Arctic', 'Arctique'), ('Atlantic', 'Atlantique'), ('Indian', 'Indien'), ('Pacific', 'Pacifique')], max_length=50)),
                ('speed', models.FloatField(help_text='Vitesse du courant en m/s')),
                ('temperature', models.FloatField(help_text="Température de l'eau en degrès(°C)")),
                ('salinity', models.FloatField(help_text='Salinité en PSU')),
                ('force', models.FloatField(help_text='Force du courant (coeff)')),
                ('direction', models.CharField(help_text='Direction du courant', max_length=50)),
                ('depth', models.IntegerField(help_text='Profondeur du courant en mètres')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
