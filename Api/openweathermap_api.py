import requests
from utils.config import API_TOKEN


class OpenWeatherMapAPI:
    base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather_by_city_name(self, city_name):
        params = {"q": city_name, "appid": API_TOKEN}
        response = requests.get(f"{self.base_url}/weather", params=params)
        return response

    def get_current_weather_by_invalid_city_name(self, invalid_city_name):
        params = {"q": invalid_city_name, "appid": API_TOKEN}
        response = requests.get(f"{self.base_url}/weather", params=params)
        return response






