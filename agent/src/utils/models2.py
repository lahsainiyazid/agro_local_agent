import os
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:1.5b",
    base_url=os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )
)
