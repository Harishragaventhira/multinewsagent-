from agents.base_agent import fetch_topic_news

def fetch_time_series_news():
    return fetch_topic_news(
        display_name="Time Series Forecasting",
        query='"time series forecasting" OR "sequence prediction" OR "autoregressive model"'
    )
