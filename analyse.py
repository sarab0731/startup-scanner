from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyse_startups(articles, industry, location, role_type, interests):
    content = "\n".join([
        f"Title: {a['title']}\nSummary: {a['summary']}"
        for a in articles
    ])

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {
                "role": "system",
                "content": """You are a career advisor helping junior candidates find opportunities at startups.
                
Only include companies that are based in or have a significant office in {location}.
If you are not confident a company is based there, exclude it.

Extract company names from the articles and score each one.
Return ONLY a JSON array, no other text, no markdown, no backticks.

Each object must have exactly these fields:
{
    "company": "Company name",
    "score": 85,
    "reason": "One line explaining why this company is a good match",
    "what_they_do": "Two sentence description of the company",
    "culture": "Two sentence summary of work environment and culture",
    "hiring_signals": "Why this company looks like it may be hiring",
    "recent_news": "Most relevant recent news about this company"
}"""
            },
            {
                "role": "user",
                "content": f"""Articles:
{content}

User is looking for: {role_type} roles in {industry} in {location}
Their interests are: {interests}

Articles:
{content}
Only include companies actually based in {location}. Exclude any companies that are not.
Return a JSON array of 3-5 companies scored on growth, culture and relevance to the interests above."""

            }
        ]
    )

    raw = response.choices[0].message.content
    return json.loads(raw)

if __name__ == "__main__":
    from fetch import get_startup_news
    articles = get_startup_news("AI", "London")
    results = analyse_startups(
        articles,
        industry="AI",
        location="London",
        role_type="Internship",
        interests="machine learning, product design"
    )
    print(results)  # add this
    for company in results:
        print(company.keys())  # and this - shows exact field names
        break