from agents.base_agent import fetch_topic_news

def fetch_computing_news():
    return fetch_topic_news(
        display_name="Computing Agent",
        query='"quantum computing" OR "high performance computing" OR "supercomputer" OR "GPU computing" OR "hardware acceleration" OR "TPU" OR "AI chip"'
    )
