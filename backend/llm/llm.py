import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load local environment variables from .env
load_dotenv()

# 1. Initialize the LangChain Model for Groq
llm = ChatOpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.3-70b-versatile",
    temperature=0.0
)

# 2. Define the Prompt Template
prompt_template = PromptTemplate.from_template(
    """You are an AI news analyst.

Your task:
- Summarize ONLY {category} news.
- Provide detailed and comprehensive bullet points explaining the news context, details, and implications.
- Do not mention topics outside of the {category} category.
- Do not apologize or state what type of headlines these are not.
- Keep the summary professional, clear, and informative.

News Headlines:
{news_text}"""
)

# 3. Create the LCEL Chain (Prompt -> LLM)
news_chain = prompt_template | llm

def summarize_news(news_text, category):
    # 4. Invoke the chain
    response = news_chain.invoke({
        "category": category, 
        "news_text": news_text
    })
    return response.content