import pytest
from Api.openweathermap_api import OpenWeatherMapAPI


class TestOpenWeatherMapApi:
    @pytest.fixture()
    def api(self):
        return OpenWeatherMapAPI()

    @pytest.mark.parametrize("city_name", ["London", "New York", "Tokyo"])
    def test_get_current_weather_by_city_name(self, api, city_name):
        response = api.get_current_weather_by_city_name(city_name)
        assert response.status_code == 200
        response.raise_for_status()
        assert "weather" in response.json()

    @pytest.mark.parametrize("invalid_city_name", ["InvalidCity1", "InvalidCity2", "InvalidCity3"])
    def test_get_current_weather_by_invalid_city_name(self, api, invalid_city_name):
        response = api.get_current_weather_by_city_name(invalid_city_name)
        assert response.status_code == 404
