from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user

from webapp.forms import LoginForm
from webapp.model import db, News, User
from webapp.weather import get_weather_by_city


def create_app():
    # создаём Flask-приложение
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

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

    # старница для логина
    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    # авторизация на сайте
    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы успешно вошли на сайт')
                return redirect(url_for('index'))

        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    # завершение сессии пользователя
    @app.route('/logout')
    def logout():
        flash('Вы успешно разлогинились на сайте')
        logout_user()
        return redirect(url_for('index'))

    return app
