import json

import requests

from config import Config

class Weather:

    def __init__(self):

        self.base_url = 'http://api.openweathermap.org/data/2.5/onecall?id={}&appid={}&units={}'
        self.current_weather_url_id = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units={}'
        self.api_key = Config.API_KEY
        self.units = 'imperial'
        self.city_id = 0
        self.cities = {}

    def list_city_by_name(self, city_name):

        possible_cities = []

        with open('city.list.json', encoding="utf8") as fo:
            data = json.load(fo)

        for item in data:
            if item['country'] == 'US':
                self.cities[item['id']] = item['name'] + ', ' + item['state']

        for item in self.cities.keys():
            if city_name.lower() in self.cities[item].lower():
                possible_cities.append(self.cities[item])

        return possible_cities

    def current_weather_id(self):

        output = {}

        self.url = self.current_weather_url_id.format(self.city_id, self.api_key, self.units)

        r = requests.get(self.url)

        if r.status_code == 200:
            data = json.loads(r.text)
            temp = data['main']['temp']
            min_temp = data['main']['temp_min']
            max_temp = data['main']['temp_max']

            output['temp'] = temp
            output['min'] = min_temp
            output['max'] = max_temp

            return output