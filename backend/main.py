# Import all 20 separate agent functions individually
from agents.machine_learning_agent import fetch_machine_learning_news
from agents.deep_learning_agent import fetch_deep_learning_news
from agents.generative_ai_agent import fetch_generative_ai_news
from agents.nlp_agent import fetch_nlp_news
from agents.computer_vision_agent import fetch_computer_vision_news
from agents.llms_agent import fetch_llms_news
from agents.agentic_ai_agent import fetch_agentic_ai_news
from agents.reinforcement_learning_agent import fetch_reinforcement_learning_news
from agents.rag_agent import fetch_rag_news
from agents.ai_automation_agent import fetch_ai_automation_news
from agents.mlops_agent import fetch_mlops_news
from agents.data_science_agent import fetch_data_science_news
from agents.neural_networks_agent import fetch_neural_networks_news
from agents.transformers_agent import fetch_transformers_news
from agents.prompt_engineering_agent import fetch_prompt_engineering_news
from agents.ai_ethics_agent import fetch_ai_ethics_news
from agents.speech_ai_agent import fetch_speech_ai_news
from agents.recommendation_systems_agent import fetch_recommendation_systems_news
from agents.time_series_agent import fetch_time_series_news
from agents.anomaly_detection_agent import fetch_anomaly_detection_news
from agents.cloud_agent import fetch_cloud_news
from agents.api_agent import fetch_api_news
from agents.computing_agent import fetch_computing_news

AGENT_RUNNERS = [
    ("Machine Learning", fetch_machine_learning_news),
    ("Deep Learning", fetch_deep_learning_news),
    ("Generative AI", fetch_generative_ai_news),
    ("Natural Language Processing (NLP)", fetch_nlp_news),
    ("Computer Vision", fetch_computer_vision_news),
    ("Large Language Models (LLMs)", fetch_llms_news),
    ("Agentic AI", fetch_agentic_ai_news),
    ("Reinforcement Learning", fetch_reinforcement_learning_news),
    ("Retrieval-Augmented Generation (RAG)", fetch_rag_news),
    ("AI Automation", fetch_ai_automation_news),
    ("MLOps", fetch_mlops_news),
    ("Data Science", fetch_data_science_news),
    ("Neural Networks", fetch_neural_networks_news),
    ("Transformers", fetch_transformers_news),
    ("Prompt Engineering", fetch_prompt_engineering_news),
    ("AI Ethics & Responsible AI", fetch_ai_ethics_news),
    ("Speech AI", fetch_speech_ai_news),
    ("Recommendation Systems", fetch_recommendation_systems_news),
    ("Time Series Forecasting", fetch_time_series_news),
    ("Anomaly Detection", fetch_anomaly_detection_news),
    ("Cloud Agent", fetch_cloud_news),
    ("API Agent", fetch_api_news),
    ("Computing Agent", fetch_computing_news)
]

def run_all_agents():
    print("\n==============================")
    print("AI MULTI-AGENT NEWS SYSTEM")
    print("==============================\n")

    summaries = {}

    # Run each agent
    for display_name, agent_fn in AGENT_RUNNERS:
        print(f"Starting {display_name} Agent...")
        summaries[display_name] = agent_fn()
        print("\n==================================\n")

    print("\n==============================")
    print("FINAL AI NEWS HUB REPORT")
    print("==============================\n")

    for display_name, _ in AGENT_RUNNERS:
        print(f"{display_name.upper()} NEWS SUMMARY:\n")
        print(summaries[display_name])
        print("\n----------------------------------\n")

if __name__ == "__main__":
    run_all_agents()