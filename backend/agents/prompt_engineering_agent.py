from agents.base_agent import fetch_topic_news

def fetch_prompt_engineering_news():
    return fetch_topic_news(
        display_name="Prompt Engineering",
        query='"prompt engineering" OR "few-shot prompting" OR "system prompt" OR "in-context learning"'
    )
