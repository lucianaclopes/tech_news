from tech_news.database import db


# Requisito 7
def search_by_title(title):
    """Seu código deve virnsitive aqui"""
    title_insensitive = title.lower()
    news = db.news.find({"title": {"$regex": title_insensitive, "$options": "i"}})
    answer = [(item["title"], item["url"]) for item in news]
    return answer


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
