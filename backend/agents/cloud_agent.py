from agents.base_agent import fetch_topic_news

def fetch_cloud_news():
    return fetch_topic_news(
        display_name="Cloud Agent",
        query='"cloud computing" OR "cloud AI" OR "AWS" OR "Azure" OR "Google Cloud" OR "GCP" OR "cloud infrastructure"'
    )
