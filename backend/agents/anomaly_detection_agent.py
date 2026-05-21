from agents.base_agent import fetch_topic_news

def fetch_anomaly_detection_news():
    return fetch_topic_news(
        display_name="Anomaly Detection",
        query='"anomaly detection" OR "outlier detection" OR "fraud detection AI"'
    )
