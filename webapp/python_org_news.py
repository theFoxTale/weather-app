from bs4 import BeautifulSoup
import requests

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
    news_list = []
    for news in all_news:
        title = news.find('a').text
        url = news.find('a')['href']
        date_published = news.find('time').text
        news_list.append({
            "title": title,
            "url": url,
            "published": date_published
        })
    return news_list
