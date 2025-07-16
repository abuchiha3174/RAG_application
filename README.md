# LangChain RAG Chatbot (LLM-Powered Prompt System)

This is a demonstration of my applied skills in using LLMs for structured data extraction, dynamic prompt creation, and full-stack delivery. It integrates prompt engineering, schema-aware NER, and real-time LLM interaction via a Flask web app.

---

## ✅ Highlights (AI Engineer / Data Scientist / Researcher Perspective)

* 🔍 **Schema-Aware NER with LLMs**: Custom prompt templates exatract relevant fields like `domain`, `method`, `framework`, etc. using GPT models. Easily extendable for research/data pipelines.
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

## 📌 Key Code Components

### 🧩 `DataIngestionLoader`
* Handles both file and URL input  
* Supports `.pdf`, `.txt`, `.csv`, `.json`, `.docx`, `.html`, and web pages  
* Internally uses LangChain’s document loaders

### 🧠 `SchemaNER`
* LLM-powered schema-based entity extraction using OpenAI  
* Returns structured JSON fields used in prompts

### 🧾 `PromptBuilder`
* Dynamically injects extracted fields into a system/user prompt  
* Enables context-rich, personalized responses

---

## 💼 Why This Matters

This project demonstrates:

* 🛠 How to build LLM applications with structured input/output  
* 🧠 How to extract interpretable, reusable metadata using schema prompts  
* ⚙️ How to combine prompt engineering, context injection, and LangChain pipelines  
* 📊 How to log and evaluate generation quality using prompt traces  
* 🚀 How to set up full-stack AI workflows (LLM + web UI + document ingestion)

---

## 🧱 Planned Additions

* [ ] Document chunking + vector embeddings (full RAG)  
* [ ] LangSmith or Phoenix tracing integration  
* [ ] Streamlit/Gradio UI version  
* [ ] PDF/JSON export of results  
* [ ] API endpoints for backend-only integration  

---

## 📬 Contact

Feel free to reach out if you're looking for a hands-on AI Engineer / Researcher with:

* Experience building LLM applications from scratch  
* Knowledge of prompt + context engineering  
* Practical backend + frontend integration skills  
* A passion for building real-world, user-facing AI tools

---

## 📄 License

MIT

---

> Built with ❤️ using LangChain, Flask, OpenAI, and too many cups of ☕.
