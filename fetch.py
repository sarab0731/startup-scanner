import feedparser
from urllib.parse import quote

def get_startup_news(query):
    encoded_query = quote(query)
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-GB&gl=GB&ceid=GB:en"
    feed = feedparser.parse(url)
    
    results = []
    for entry in feed.entries[:5]: 
        results.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary,
            "published": entry.published
        })
    
    return results

# Test
if __name__ == "__main__":
    news = get_startup_news("London startup funding 2026")
    print(f"Found {len(news)} articles")
    for item in news:
        print(item["title"])
        print(item["published"])
        print("---")