from agents.base_agent import fetch_topic_news

def fetch_ai_ethics_news():
    return fetch_topic_news(
        display_name="AI Ethics & Responsible AI",
        query='"AI ethics" OR "responsible AI" OR "AI safety" OR "AI alignment" OR "bias mitigation"'
    )
