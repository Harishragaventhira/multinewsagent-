from agents.base_agent import fetch_topic_news

def fetch_transformers_news():
    return fetch_topic_news(
        display_name="Transformers",
        query='"transformer architecture" OR "attention mechanism" OR "vision transformer" OR "BERT"'
    )
