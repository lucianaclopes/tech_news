from parsel import Selector
from tech_news.database import create_news
import time
import requests
import re


# Requisito 1 modificando para fazer o commit inicial do projeto
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(
            url,
            headers={'User-Agent': 'Fake User Agent', 'Accept': 'text/html'},
            timeout=3
        )
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_links = selector.css(
        'h2.entry-title a::attr(href)'
        ).getall()
    if news_links:
        return news_links
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page = selector.css(
        'a.next.page-numbers::attr(href)'
        ).get()
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css(
        'h1.entry-title::text'
        ).get().strip()
    timestamp = selector.css(
        'li.meta-date::text'
        ).get()
    writer = selector.css(
        'span.fn a::text'
        ).get().strip()
    reading_time_text = selector.css(
        'li.meta-reading-time::text'
        ).get()
    reading_time = re.search(r'\d+', reading_time_text).group()

    summary = (
        "".join(selector.css('div.entry-content > p:first-of-type *::text')
                .getall())
    ).strip()
    category = selector.css('span.label::text').get()

    return {
            'url': url,
            'title': title,
            'timestamp': timestamp,
            'writer': writer,
            'reading_time': int(reading_time),
            'summary': summary,
            'category': category
                }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = 'https://blog.betrybe.com/'
    news = []
    while len(news) < amount:
        html_content = fetch(url)
        news_links = scrape_updates(html_content)
        for link in news_links:
            news_html = fetch(link)
            if len(news) == amount:
                break
            news_details = scrape_news(news_html)
            news.append(news_details)

        next_page = scrape_next_page_link(html_content)
        if not next_page:
            break
        url = next_page
    create_news(news)
    return news
