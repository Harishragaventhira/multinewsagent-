from agents.base_agent import fetch_topic_news

def fetch_computer_vision_news():
    return fetch_topic_news(
        display_name="Computer Vision",
        query='"computer vision" OR "image recognition" OR "object detection" OR "YOLO"'
    )
