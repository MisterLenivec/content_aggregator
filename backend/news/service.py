from bs4 import BeautifulSoup
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()

from news.models import Article, SiteBoard


def get_techcrunch_articles():
    site_board_name = SiteBoard.objects.get(site_name='TechCrunch')
    Article.objects.filter(site_board=site_board_name).delete()
    response = requests.get('https://techcrunch.com/')
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    for post in soup.find_all(class_='post-block--unread')[:10]:
        article = Article(
            title=post.find('a', class_='post-block__title__link').get_text().strip(),
            description=post.find('div', class_='post-block__content').get_text().strip(),
            url=post.find('a', class_='post-block__title__link').get('href'),
            site_board=site_board_name
        )
        article.save()


get_techcrunch_articles()


# bs4 a lot faster than selenium.

# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# # import time
#
#
# def chrome_options():
#     options = Options()
#     options.add_argument("--headless")  # No open browser
#     options.add_argument("--window-size=1920x1080")
#     return options
#
#
# browser = webdriver.Chrome(options=chrome_options())
#
#
# def get_element_text(how, name):
#     WebDriverWait(browser, 5).until(
#         EC.presence_of_element_located((how, name)))
#     try:
#         return str(browser.find_element(how, name).text)
#     except NoSuchElementException:
#         return None
#
#
# def get_techcrunch_article():
#     link = 'https://techcrunch.com/'
#     browser.get(link)
#     attempts = 0
#     while attempts < 2:
#         try:
#             art = []
#             # browser.implicitly_wait(5)
#             articles = browser.find_elements_by_css_selector("article.post-block")[:10]
#             for article in articles:
#                 article.click()
#                 art.append(get_element_text(By.CLASS_NAME, "article__title"))
#                 art.append(get_element_text(By.ID, "speakable-summary"))
#                 art.append(browser.current_url)
#             for i in art:
#                 print(i)
#             break
#         except StaleElementReferenceException:
#             print("StaleElementReferenceException let's try 1-2 times")
#             attempts += 1
#         finally:
#             browser.quit()
#
#
# get_techcrunch_article()