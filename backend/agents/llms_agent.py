from agents.base_agent import fetch_topic_news

def fetch_llms_news():
    return fetch_topic_news(
        display_name="Large Language Models (LLMs)",
        query='"large language model" OR "LLM" OR "GPT-4" OR "Claude 3" OR "Llama 3" OR "Gemini 1.5"'
    )
