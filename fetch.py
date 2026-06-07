import feedparser
from urllib.parse import quote

from datetime import datetime


def get_startup_news(industry, location):
    # Search for startups based on industry and location
    query = quote(f"{industry} startup {location} {datetime.now().year}")
    
    feeds = [
        f"https://news.google.com/rss/search?q={query}&hl=en-GB&gl=GB&ceid=GB:en",
        f"https://sifted.eu/feed?s={query}",
        f"https://www.eu-startups.com/feed/?s={query}",
    ]
    
    results = []
    seen_titles = set()  # avoid duplicates
    
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:
            if entry.title not in seen_titles:
                seen_titles.add(entry.title)
                results.append({
                    "title": entry.title,
                    "summary": entry.get("summary", "No summary available"),
                    "link": entry.get("link", ""),
                    "published": entry.get("published", "Unknown date")
                })
    
    return results

if __name__ == "__main__":
    articles = get_startup_news("AI", "London")
    print(f"Found {len(articles)} articles")
    for a in articles:
        print(a["title"])
        print("---")