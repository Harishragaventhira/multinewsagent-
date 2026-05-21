from agents.base_agent import fetch_topic_news

def fetch_neural_networks_news():
    return fetch_topic_news(
        display_name="Neural Networks",
        query='"neural network" OR "artificial neural network" OR "CNN" OR "RNN"'
    )
