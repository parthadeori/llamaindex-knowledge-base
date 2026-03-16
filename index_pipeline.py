# Import Required Libraries
import os
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

# Load Environment Variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Create LLM
llm = Groq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY
)

# Set the Embedding Model
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

Settings.embed_model = embed_model

# Load Documents
def load_documents():
    documents = SimpleDirectoryReader("data").load_data()
    return documents

# Create the Vector Index
def create_index(documents):
    index = VectorStoreIndex.from_documents(documents)
    return index

# Create Query Engine
def get_query_engine(index):
    query_engine = index.as_query_engine(llm=llm)
    return query_engine