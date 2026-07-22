from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    print("[INFO] Starting RAG App...")
    
    # RAGSearch automatically handles loading or building the FAISS index!
    rag_search = RAGSearch()
    
    query = "What is block-chain based voting system?"
    print(f"[INFO] Querying: {query}")
    
    summary = rag_search.search_and_summarize(query, top_k=3) 
    print("\n================ SUMMARY ================")
    print(summary)
    print("=========================================\n")