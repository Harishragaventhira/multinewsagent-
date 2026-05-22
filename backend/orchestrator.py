from typing import TypedDict
from langgraph.graph import StateGraph, END
from datetime import datetime

# Import the 20 separate agent functions individually
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

# Define mappings for dynamic node construction
AGENT_FUNCTIONS = {
    "machine_learning": fetch_machine_learning_news,
    "deep_learning": fetch_deep_learning_news,
    "generative_ai": fetch_generative_ai_news,
    "nlp": fetch_nlp_news,
    "computer_vision": fetch_computer_vision_news,
    "llms": fetch_llms_news,
    "agentic_ai": fetch_agentic_ai_news,
    "reinforcement_learning": fetch_reinforcement_learning_news,
    "rag": fetch_rag_news,
    "ai_automation": fetch_ai_automation_news,
    "mlops": fetch_mlops_news,
    "data_science": fetch_data_science_news,
    "neural_networks": fetch_neural_networks_news,
    "transformers": fetch_transformers_news,
    "prompt_engineering": fetch_prompt_engineering_news,
    "ai_ethics": fetch_ai_ethics_news,
    "speech_ai": fetch_speech_ai_news,
    "recommendation_systems": fetch_recommendation_systems_news,
    "time_series": fetch_time_series_news,
    "anomaly_detection": fetch_anomaly_detection_news,
    "cloud_agent": fetch_cloud_news,
    "api_agent": fetch_api_news,
    "computing_agent": fetch_computing_news
}

# 1. Define the Shared State covering all AI categories
class NewsState(TypedDict):
    machine_learning: str
    deep_learning: str
    generative_ai: str
    nlp: str
    computer_vision: str
    llms: str
    agentic_ai: str
    reinforcement_learning: str
    rag: str
    ai_automation: str
    mlops: str
    data_science: str
    neural_networks: str
    transformers: str
    prompt_engineering: str
    ai_ethics: str
    speech_ai: str
    recommendation_systems: str
    time_series: str
    anomaly_detection: str
    cloud_agent: str
    api_agent: str
    computing_agent: str
    last_updated: str

# 2. Define Node Generator Function calling imports
def make_node(topic_key: str, agent_fn):
    def node(state: NewsState):
        summary = agent_fn()
        return {topic_key: summary}
    return node

# 3. Build the Graph
workflow = StateGraph(NewsState)

# Add Nodes dynamically using the imported functions
for key, agent_fn in AGENT_FUNCTIONS.items():
    workflow.add_node(key, make_node(key, agent_fn))

# Define Edges dynamically (Sequential Flow)
topic_keys = list(AGENT_FUNCTIONS.keys())
workflow.set_entry_point(topic_keys[0])

for i in range(len(topic_keys) - 1):
    workflow.add_edge(topic_keys[i], topic_keys[i + 1])

workflow.add_edge(topic_keys[-1], END)

# 4. Compile the Graph
news_graph = workflow.compile()

def run_agent_workflow():
    """Triggers the LangGraph execution for all 20 AI news agents"""
    print(f"\n--- LangGraph Multi-Agent Workflow Started ---")
    
    # Initialize state with empty summaries
    initial_state = {key: "" for key in AGENT_FUNCTIONS.keys()}
    initial_state["last_updated"] = ""
    
    # Run the graph and return the final state
    final_output = news_graph.invoke(initial_state)
    
    # Add final timestamp
    final_output["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return final_output
