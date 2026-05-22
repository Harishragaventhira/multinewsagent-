from agents.base_agent import fetch_topic_news

def fetch_api_news():
    return fetch_topic_news(
        display_name="API Agent",
        query='"AI API" OR "API integration" OR "REST API" OR "GraphQL" OR "Web APIs" OR "microservices" OR "developer APIs"'
    )
