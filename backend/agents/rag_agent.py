from agents.base_agent import fetch_topic_news

def fetch_rag_news():
    return fetch_topic_news(
        display_name="Retrieval-Augmented Generation (RAG)",
        query='"retrieval-augmented generation" OR "RAG" OR "vector database" OR "embeddings"'
    )
