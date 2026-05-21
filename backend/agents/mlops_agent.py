from agents.base_agent import fetch_topic_news

def fetch_mlops_news():
    return fetch_topic_news(
        display_name="MLOps",
        query='"MLOps" OR "machine learning operations" OR "model registry" OR "data drift"'
    )
