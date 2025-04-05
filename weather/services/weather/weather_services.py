import requests
from settings.config import Config


class WeatherService:
    def __init__(self):
        config = Config().get_weather_config()
        self.api_key = config["api_key"]
        self.base_url = config["base_url"]
        self.api_host = config["api_host"]
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.api_host
        }

    def get_weather(self, city: str) -> dict:
        params = {"q": city}
        response = requests.get(self.base_url, headers=self.headers, params=params)

        if response.status_code != 200:
            raise Exception(f"Weather API request failed: {response.text}")

        data = response.json()
        current = data["current"]
        location = data["location"]

        return {
            "weather": f"{current['temp_c']} C",
            "latitude": str(location["lat"]),
            "longitude": str(location["lon"]),
            "city": f"{location['name']} {location['country']}"
        }
