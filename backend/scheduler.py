from apscheduler.schedulers.background import BackgroundScheduler
from orchestrator import run_agent_workflow

news_data = {}

def update_news():
    global news_data
    # This triggers the LangGraph multi-agent orchestration
    news_data = run_agent_workflow()
    print(f"\n--- LangGraph Workflow Completed Successfully ---\n")

scheduler = BackgroundScheduler()

# Set update interval to 15 minutes
scheduler.add_job(update_news, "interval", minutes=60)

def start_scheduler():
    update_news()
    scheduler.start()

print("Agentic Scheduler Started...")
