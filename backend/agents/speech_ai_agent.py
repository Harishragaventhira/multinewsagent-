from agents.base_agent import fetch_topic_news

def fetch_speech_ai_news():
    return fetch_topic_news(
        display_name="Speech AI",
        query='"speech recognition" OR "voice synthesis" OR "text to speech" OR "Whisper AI" OR "TTS"'
    )
