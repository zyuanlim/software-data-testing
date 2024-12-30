from typing import Dict

import requests


def get_weather(latitude: float = 22.3193, longitude: float = 114.1694) -> Dict:
    """
    Function to get weather using Open-Meteo API
    :param latitude: Location latitude (defaults to Hong Kong)
    :param longitude: Location longitude (defaults to Hong Kong)
    :return: Weather data for the specified coordinates
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=Asia%2FHong_Kong"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
