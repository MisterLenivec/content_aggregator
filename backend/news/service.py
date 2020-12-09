from bs4 import BeautifulSoup
import traceback
import requests
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()
from django.core.mail import send_mail
from django.contrib.auth.models import User

from backend.settings import EMAIL_HOST_USER
from news.models import Article, SiteBoard


headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'}


def send_message_about_problems(ex, site_name='Wired'):
    send_mail(
        'Wake up, Neo... We are fucked up! Content aggregator problem!',
        f'Possible problem with {site_name} in data.json.\n '
        f'{ex.__class__.__name__}, {ex}.\n\n '
        f'{traceback.format_exc()}',
        EMAIL_HOST_USER,
        [User.objects.get(is_superuser=True).email],
        fail_silently=False,
    )


def get_articles(site):
    """Universal parser for multiple sites"""
    site_board_name = SiteBoard.objects.get(site_name=site['site_name'])
    Article.objects.filter(site_board=site_board_name).delete()
    response = requests.get(site['site_board_url'], headers=headers)
    soup = BeautifulSoup(response.text, features='html.parser')
    for post in soup.find_all(class_=site['card_class'])[:10]:
        article = Article(
            title=post.find(site['title_tag'], class_=site['title_class']).get_text().strip(),
            description=post.find(site['descr_tag'], class_=site['descr_class']).get_text().strip() if site['descr_tag'] else 'Read more in this article',
            url=post.find(site['url_tag'], class_=site['url_class']).get('href'),
            site_board=site_board_name
        )
        article.save()


# You're the chosen one, ha?
def get_wired_articles():
    """Parser for Wired"""
    site_board_name = SiteBoard.objects.get(site_name='Wired')
    Article.objects.filter(site_board=site_board_name).delete()
    response = requests.get('https://www.wired.com/', headers=headers)
    soup = BeautifulSoup(response.text, features='html.parser')
    for post in soup.find_all(class_='card-component__description')[:10]:
        article = Article(
            title=post.find('h2').get_text().strip(),
            description=post.find('span').get_text().strip(),
            url=post.find('a').get('href') if 'http' in post.find('a').get('href') else 'https://www.wired.com' + post.find('a').get('href'),
            site_board=site_board_name
        )
        article.save()


def start_parsing():
    """Read json data and start parsing"""
    try:
        get_wired_articles()
    except AttributeError:
        print(traceback.format_exc())
        send_message_about_problems(AttributeError)

    try:
        with open("news/data.json", "r") as read_file:
            search_data = json.load(read_file)
            for site in search_data:
                try:
                    get_articles(search_data[site])
                except AttributeError:
                    print(traceback.format_exc())
                    send_message_about_problems(AttributeError, search_data[site]["site_name"])
    except FileNotFoundError:
        print(traceback.format_exc())
        send_message_about_problems(FileNotFoundError, 'reading data')
