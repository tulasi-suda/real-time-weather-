import requests
from datetime import datetime
from config import Config

class WeatherAPIError(Exception):
    pass

class WeatherClient:
    def __init__(self, api_key=Config.API_KEY, base_url=Config.BASE_URL, timeout=Config.REQUEST_TIMEOUT):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=self.timeout)
            data = response.json()

            if response.status_code != 200:
                raise WeatherAPIError(data.get("message", "Failed to fetch weather"))

            return {
                "city": city.title(),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "condition": data["weather"][0]["description"],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

        except requests.exceptions.Timeout:
            raise WeatherAPIError("API request timed out.")
        except requests.exceptions.ConnectionError:
            raise WeatherAPIError("Network connection error.")
