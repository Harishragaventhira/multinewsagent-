from agents.base_agent import fetch_topic_news

def fetch_ai_automation_news():
    return fetch_topic_news(
        display_name="AI Automation",
        query='"AI automation" OR "RPA" OR "automated workflow" OR "AI copilot"'
    )
