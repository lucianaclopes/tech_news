from parsel import Selector
import time
import requests


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
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
