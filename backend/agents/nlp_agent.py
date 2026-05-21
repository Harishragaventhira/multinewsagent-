from agents.base_agent import fetch_topic_news

def fetch_nlp_news():
    return fetch_topic_news(
        display_name="Natural Language Processing (NLP)",
        query='"natural language processing" OR "NLP" OR "text generation" OR "sentiment analysis"'
    )
