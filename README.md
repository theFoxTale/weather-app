# Учебный проект по треку "Вёб-разработка"

Программа сохраняет новости с сайта [python.org](https://www.python.org/blogs/) в БД, выводит их на экран и показывает текущую погоду в Москве.

## Установка программы

1. Клонируйте репозиторий с сайта GitHub
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл webapp\config.py и создайте в нем переменные:
    ```
    API_KEY = Ключ API с сайта http://api.worldweatheronline.com
    DEFAULT_CITY = Город, для которого отображается погода (например, "Moscow,Russia")
    WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'webapp.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
    ```

## Запуск программы

Для запуска программы в командной строке выполните код:
```
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```

И откройте в браузере вкладку с адресом http://127.0.0.1:5000/