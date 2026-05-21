from agents.base_agent import fetch_topic_news

def fetch_machine_learning_news():
    return fetch_topic_news(
        display_name="Machine Learning",
        query='"machine learning" OR "ML" OR "machine-learning"'
    )
