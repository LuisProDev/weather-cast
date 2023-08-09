import requests
import keys


class WeatherSys:
    def __init__(self):
        api_key = keys.api_key

        geo_loc = requests.get(url=f"http://api.openweathermap.org/geo/1.0/direct?q=Brasília,"
                                   f" Federal District &limit=5&appid={api_key}")
        geo_loc.raise_for_status()
        geo_data = geo_loc.json()
        self.user_lat = geo_data[0]['lat']
        self.user_long = geo_data[0]["lon"]
        print(self.user_lat, self.user_long)

        weather_key = keys.weather_key
        wheather_endp = "http://api.weatherapi.com/v1/forecast.json"
        wheather_param = {
            "q": (self.user_lat,self.user_long),
            'key': weather_key,
            "days": 7,
            "hour": 16
        }

        weather_connection = requests.get(wheather_endp, params=wheather_param)
        weather_connection.raise_for_status()
        weather_data = weather_connection.json()

        self.seven_days = []
        for i in range(0, 7):
            self.seven_days.append(weather_data['forecast']['forecastday'][i]['day']['condition'])
