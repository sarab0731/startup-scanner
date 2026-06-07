from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyse_articles(articles):
    # Combine article titles and summaries into one block of text
    content = "\n".join([
        f"Title: {a['title']}\nSummary: {a['summary']}"
        for a in articles
    ])

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {
                "role": "system",
                "content": "You are a startup analyst. Analyse the following news articles and return a short summary of the startup activity and an opportunity score from 0-100."
            },
            {
                "role": "user",
                "content": content
            }
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    # Test
    test_articles = [
        {"title": "London AI startup raises £10M", "summary": "A new AI company secured funding to expand their team."},
        {"title": "Fintech firm opens new London office", "summary": "Growing fintech company announces 200 new hires."}
    ]
    print(analyse_articles(test_articles))