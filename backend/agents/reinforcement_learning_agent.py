from agents.base_agent import fetch_topic_news

def fetch_reinforcement_learning_news():
    return fetch_topic_news(
        display_name="Reinforcement Learning",
        query='"reinforcement learning" OR "RL" OR "deep Q-learning" OR "policy gradient"'
    )
