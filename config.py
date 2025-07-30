

# === config.py ===
def get_llm():
    from langchain_ollama import OllamaLLM
    return OllamaLLM(model="ollama/mistral:latest", base_url="http://127.0.0.1:11435")  # Optimized for CPU

def get_embedder_config():
    return {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text:latest",
            "base_url": "http://127.0.0.1:11435"
        }
    }

def reset_memory():
    import chromadb
    client = chromadb.PersistentClient(path=".chroma")
    for name in ["short_term", "entities"]:
        try:
            client.delete_collection(name)
            print(f"🧹 Deleted memory collection: {name}")
        except Exception:
            pass

