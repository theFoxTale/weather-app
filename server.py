from flask import Flask, send_file
from weather import get_weather_by_city

# создаём Flask-приложение
app = Flask(__name__)

# маршрутизация в приложении
# "/" - главная страница сайта
@app.route("/")
def hello():
    msk_weather = get_weather_by_city("Moscow,Russia")
    if msk_weather:
        return (f"Сейчас в Москве {msk_weather['temp_C']}, ощущается как {msk_weather['FeelsLikeC']}")
    return ("Сервис погоды временно недоступен!")
    
@app.route('/favicon.ico')
def favicon():
    return send_file('favicon.ico')

if __name__ == "__main__":
    app.run(debug=True)
