# backend/agents/base_agent.py

import os
import requests
from dotenv import load_dotenv
from llm.llm import summarize_news

# Load local environment variables from .env
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_topic_news(display_name: str, query: str):
    print(f"\nFetching {display_name} News...\n")
    
    # We use everything endpoint to search specific AI subtopics
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if response.status_code != 200:
            print(f"Error fetching {display_name} news: {data.get('message', 'Unknown error')}")
            return f"No {display_name.lower()} news available at the moment"
            
        articles = data.get("articles", [])
        
        if not articles:
            print("No articles found")
            return f"No recent {display_name.lower()} news available"
            
        news_text = ""
        print(f"Top {display_name} Headlines:\n")
        
        for article in articles[:5]:
            title = article.get("title", "No Title")
            description = article.get("description", "")
            content = article.get("content", "")
            print(f"- {title}")
            news_text += f"Title: {title}\nDescription: {description}\nContent: {content}\n\n"
            
        print(f"\nSending {display_name} News To AI...\n")
        summary = summarize_news(news_text, display_name)
        return summary
        
    except Exception as e:
        print("Error:", e)
        return f"{display_name} agent failed: {str(e)}"
