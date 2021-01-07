from flask import current_app
import requests


def get_weather_by_city(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params = {
        "key": current_app.config['API_KEY'],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }

    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()

        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except (TypeError, IndexError):
                    return False
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

    return False
