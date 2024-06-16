"""
Dieses Modul enthält Funktionen zum Abrufen geospezifischer Daten von APIs.
Es ermöglicht das Abrufen von Windgeschwindigkeit, Temperatur, relativer Luftfeuchtigkeit und Höhe für einen bestimmten Satz von Koordinaten.

Autor: Albert Grigoryan
"""

import requests

def get_wind_speed(latitude, longitude):
    """
    Abrufen der aktuellen Windgeschwindigkeit an einem bestimmten Breiten- und Längengrad mithilfe der Open-Meteo API.

    Argumente:
    latitude (float): Breitengrad des Standorts.
    longitude (float): Längengrad des Standorts.

    Rückgabe:
    float: Aktuelle Windgeschwindigkeit in Metern pro Sekunde am angegebenen Standort.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=wind_speed_10m"
    response = requests.get(url)
    response_data = response.json()
    return response_data['current']['wind_speed_10m']

def get_temperature_and_humidity(latitude, longitude):
    """
    Abrufen der aktuellen Temperatur und relativen Luftfeuchtigkeit an einem bestimmten Breiten- und Längengrad mithilfe der Open-Meteo API.

    Argumente:
    latitude (float): Breitengrad des Standorts.
    longitude (float): Längengrad des Standorts.

    Rückgabe:
    dict: Ein Wörterbuch mit Temperatur in °C und relativer Luftfeuchtigkeit in %.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m"
    response = requests.get(url)
    response_data = response.json()
    temperature_humidity = {
        'temperature_celsius': response_data['current']['temperature_2m'],
        'humidity_percent': response_data['current']['relative_humidity_2m']
    }
    return temperature_humidity

def get_elevation(latitude, longitude):
    """
    Abrufen der Höhe in Metern an einem bestimmten Breiten- und Längengrad mithilfe der Open Elevation API.

    Argumente:
    latitude (float): Breitengrad des Standorts.
    longitude (float): Längengrad des Standorts.

    Rückgabe:
    int: Höhe in Metern an den angegebenen Koordinaten.
    """
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}"
    response = requests.get(url)
    response_data = response.json()
    results = response_data['results'][0]  # Annahme, dass die Antwort für einen einzelnen Standort
    return results['elevation']
