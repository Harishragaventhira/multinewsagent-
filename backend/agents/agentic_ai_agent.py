from agents.base_agent import fetch_topic_news

def fetch_agentic_ai_news():
    return fetch_topic_news(
        display_name="Agentic AI",
        query='"agentic AI" OR "AI agents" OR "multi-agent system" OR "AI agent"'
    )
