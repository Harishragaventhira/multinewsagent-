from agents.base_agent import fetch_topic_news

def fetch_deep_learning_news():
    return fetch_topic_news(
        display_name="Deep Learning",
        query='"deep learning" OR "deep neural network" OR "backpropagation"'
    )
