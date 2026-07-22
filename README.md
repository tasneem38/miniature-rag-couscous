# RAG Application

This is a custom Retrieval-Augmented Generation (RAG) application built with Python. It allows you to ingest documents, create vector embeddings, and query them using a Large Language Model (LLM) to generate contextually accurate summaries and answers.

## Architecture

*   **Vector Database:** [FAISS](https://github.com/facebookresearch/faiss) for local, fast semantic search.
*   **Embedding Model:** `all-MiniLM-L6-v2` via Sentence Transformers.
*   **LLM API:** [Groq](https://groq.com/) using the `gemma2-9b-it` model for lightning-fast inference.
*   **Orchestration:** Containerized with Docker and Docker Compose.

## Prerequisites

1.  **Docker:** Make sure Docker and Docker Compose are installed on your machine.
2.  **Groq API Key:** Get a free API key from the [Groq Console](https://console.groq.com/).

## Setup Instructions

1. **Clone the repository.**
2. **Add your documents:** Place your source data (text/PDFs) into the `data/` directory.
3. **Environment Variables:** Create a `.env` file in the root directory and add your Groq API key:
   ```bash
   GROQ_API_KEY=your_actual_api_key_here
   ```

## Running the Application

To build and run the application using Docker, execute:

```bash
docker compose up --build
```

This will:
* Build the `rag_app` container.
* Ingest the documents from the `data/` directory.
* Create local FAISS embeddings (stored in `faiss_store/`).
* Expose the application locally.

## Project Structure

*   `src/`: Contains the main source code (vector store logic, search logic).
*   `data/`: Directory containing source documents for retrieval.
*   `faiss_store/`: Auto-generated directory where the FAISS index and metadata are persisted.
*   `app.py`: Main application entry point.
*   `docker-compose.yml` / `Dockerfile`: Environment and container configuration.
