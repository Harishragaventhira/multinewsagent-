from agents.base_agent import fetch_topic_news

def fetch_generative_ai_news():
    return fetch_topic_news(
        display_name="Generative AI",
        query='"generative AI" OR "GenAI" OR "ChatGPT" OR "generative adversarial network"'
    )
