import requests


class Weather:
    def __init__(self, token):
        self.token = token

    def fetch_weather(self, city_name):
        try:
            '''Получаем температуру в цельсиях  города'''
            data = {
                'q': city_name,
                'key': self.token,
                'p': '1',
                'd': '1',
                "lang":"ru",

            }
            url = f'http://api.weatherapi.com/v1/current.json'

            response = requests.post(url=url, data=data)
            response.raise_for_status()

            temperature = response.json()['current']['temp_c']
            return int(temperature)
        except requests.exceptions.HTTPError:
            return "Не удается получить данные о погоде "
