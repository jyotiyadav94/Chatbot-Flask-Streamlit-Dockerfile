import os
from huggingface_hub import login
from dotenv import load_dotenv, find_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.postprocessor import SentenceTransformerRerank

# Load environment variables
dotenv_path = find_dotenv(".env")
load_dotenv(dotenv_path)

# Get the HuggingFace token from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm=OpenAI(api_key = OPENAI_API_KEY,
            model_name="gpt-3.5-turbo",
            temperature=0,
            max_tokens=300)

# Load and configure models and tokenizers
documents = SimpleDirectoryReader("Data").load_data()
index = VectorStoreIndex.from_documents(documents)

rerank = SentenceTransformerRerank(model="cross-encoder/ms-marco-MiniLM-L-2-v2", top_n=3)
query_engine = index.as_query_engine(similarity_top_k=10, node_postprocessors=[rerank])

def query_model(query_str):
    """
    Query the model and return the response, utilizing the cache.
    """
    if query_str:
        response = query_engine.query(query_str)
        print(response)
        return str(response)
    return "No query provided"


if __name__ == "__main__":
    # Run the query_model function when the script is run directly
    query_model("What is the history of quantum computing?")