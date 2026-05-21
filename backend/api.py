from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import scheduler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    # Start the background scheduler from the scheduler module
    scheduler.start_scheduler()

@app.get("/news")
def get_news():
    # Return the LIVE news_data from the scheduler module
    # This ensures we see updates as they happen
    return scheduler.news_data