from agents.base_agent import fetch_topic_news

def fetch_data_science_news():
    return fetch_topic_news(
        display_name="Data Science",
        query='"data science" OR "predictive modeling" OR "pandas" OR "jupyter notebook"'
    )
