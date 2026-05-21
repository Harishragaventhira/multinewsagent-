from agents.base_agent import fetch_topic_news

def fetch_recommendation_systems_news():
    return fetch_topic_news(
        display_name="Recommendation Systems",
        query='"recommendation system" OR "recommender engine" OR "collaborative filtering" OR "matrix factorization"'
    )
