from flask import Flask, render_template

from webapp.model import db, News
from webapp.weather import get_weather_by_city


def create_app():
    # создаём Flask-приложение
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    # маршрутизация в приложении
    # "/" - главная страница сайта
    @app.route("/")
    def index():
        my_title = "Новости Python"
        msk_weather = get_weather_by_city(app.config['DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template(
            "index.html",
            page_title=my_title,
            weather=msk_weather,
            news_list=news_list
        )

    return app
