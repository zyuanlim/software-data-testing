from typing import Dict

import requests


def get_weather(latitude: float = 1.3521, longitude: float = 103.8198) -> Dict:
    """
    Function to get weather using Open-Meteo API
    :param latitude: Location latitude (defaults to Singapore)
    :param longitude: Location longitude (defaults to Singapore)
    :return: Weather data for the specified coordinates
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,wind_speed_10m,relative_humidity_2m&timezone=Asia%2FSingapore"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
