# LangChain RAG Chatbot (LLM-Powered Prompt System)

This is a demonstration of my applied skills in using LLMs for structured data extraction, dynamic prompt creation, and full-stack delivery. It integrates prompt engineering, schema-aware NER, and real-time LLM interaction via a Flask web app.

---

## ✅ Highlights (AI Engineer / Data Scientist / Researcher Perspective)

* 🔍 **Schema-Aware NER with LLMs**: Custom prompt templates extract relevant fields like `domain`, `method`, `framework`, etc. using GPT models. Easily extendable for research/data pipelines.
* 🧠 **LLM-Driven Prompt Generation**: Extracted fields populate prompt templates programmatically—core to building adaptive, context-rich LLM systems.
* 🤖 **OpenAI Integration**: Works with `gpt-3.5-turbo`, `gpt-4o`, modular for any provider (Anthropic, Mistral, Ollama, etc.).
* 🌐 **Flask-based Frontend**: Deployed as a local web interface—serves as a real-world UX for AI prototypes.
* 📦 **Pinecone Integration**: Vector DB is setup-ready for Retrieval Augmented Generation (RAG)—can scale with document ingestion.
* 📊 **LLM Output Logging**: Logs full trace of extracted fields, generated prompt, and output for downstream eval/debug.

---

## 🧠 Tech Stack

* **Python, Flask**: Web backend
* **LangChain**: Prompt orchestration and chains
* **LangChain OpenAI / Community**: Model connectors
* **Pinecone**: Vector DB (RAG-ready)
* **Dotenv**: Environment handling
* **HTML / Jinja**: Simple UI rendering

---

## 🚀 Run Locally

```bash
git clone <your-repo-url>
cd <project-directory>
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
PINECONE_KEY=your_pinecone_key
LANGCHAIN_TRACING_V2=true
```

Run the app:

```bash
python app.py
```

Open `http://localhost:5000`

---

## 🔬 Example Use Case (LLM Evaluation)

**Input:**

> "How can I use RAG with LangChain for document QA?"

**Extracted Fields:**

```json
{
  "domain": "AI",
  "method": "RAG",
  "framework": "LangChain"
}
```

**Prompt Sent to LLM:**

```
SYSTEM: You are a helpful assistant. Use available context to answer precisely.
USER: How can I use RAG with LangChain for document QA?
```

**Bot Reply:**

> "To use RAG in LangChain..."

---

## 💼 Why This Matters

This project showcases the real-world application of:

* Designing reusable prompt interfaces
* Making LLMs interpretable and context-aware
* Using extraction + inference workflows in AI systems
* Extending static NLP to dynamic field-driven interactions
* Laying foundation for tools like auto agents, tutors, and RAG pipelines

---

## 🧱 Planned Additions

* Full RAG pipeline with document chunking + embeddings
* Multi-model orchestration (OpenAI, Ollama, Claude)
* Streamlit version with interactive UI
* LangSmith integration for trace + eval
* API endpoints for scalable deployment

---

## 📬 Contact

Feel free to reach out if you're looking for a hands-on AI Engineer / Researcher with:

* LLM application design experience
* Prompt + context engineering skills
* Practical full-stack deployment knowledge

---

## 📄 License

MIT
