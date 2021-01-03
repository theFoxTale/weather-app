from flask import Flask, render_template

from webapp.python_org_news import get_python_news
from webapp.weather import get_weather_by_city

def create_app():
    # создаём Flask-приложение
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # маршрутизация в приложении
    # "/" - главная страница сайта
    @app.route("/")
    def index():
        my_title = "Новости Python"
        msk_weather = get_weather_by_city(app.config['DEFAULT_CITY'])
        news_list = get_python_news()
        return render_template("index.html", page_title=my_title, weather=msk_weather, news_list=news_list)

    return app

