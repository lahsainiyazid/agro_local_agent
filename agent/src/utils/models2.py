from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama 
from dotenv import load_dotenv,find_dotenv
import os 
_=load_dotenv(find_dotenv())
local_llm=ChatOllama(model="llama3.2:1b",temperature=0)
