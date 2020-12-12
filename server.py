from flask import Flask, render_template
from python_org_news import get_python_news
from weather import get_weather_by_city

# создаём Flask-приложение
app = Flask(__name__)

# маршрутизация в приложении
# "/" - главная страница сайта
@app.route("/")
def hello():
    my_title = "Новости Python"
    msk_weather = get_weather_by_city("Moscow,Russia")
    news_list = get_python_news()
    return render_template("index.html", page_title=my_title, weather=msk_weather, news_list=news_list)

if __name__ == "__main__":
    app.run(debug=True)
