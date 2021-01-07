from bs4 import BeautifulSoup
from datetime import datetime
import requests

from webapp.model import db, News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Возникла сетевая ошибка")
        return False


def get_python_news():
    my_html = get_html("https://www.python.org/blogs/")
    if not my_html:
        return False

    soup = BeautifulSoup(my_html, 'html.parser')
    all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
    for news in all_news:
        title = news.find('a').text
        url = news.find('a')['href']

        date_published = news.find('time').text
        try:
            date_published = datetime.strptime(date_published, '%b. %d, %Y')
        except ValueError:
            date_published = datetime.now()

        save_news_in_db(title, url, date_published)


def save_news_in_db(title, url, published):
    is_news_exist = News.query.filter(News.url == url).count()
    if not is_news_exist:
        my_news = News(title=title, url=url, published=published)
        db.session.add(my_news)
        db.session.commit()
