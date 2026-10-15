# AccuKnox AI/ML Assessment — Tanishq Gupta

This repository contains the complete submission for the AccuKnox AI/ML technical assessment, covering Problem Statement 1 (Python, API, Database, Visualization) and Problem Statement 2 (LLM, Deep Learning, AI, ML theory).

**Author:** Tanishq Gupta — `Tanishqg503@gmail.com` — (https://github.com/02tanishq)
**Date:** october 2026

---

## Repository Structure

```
accuknox-ai-ml-assessment/
├── problem_statement_1/          # Implementation tasks
│   ├── 01_api_to_sqlite.py       # API → SQLite (books)
│   ├── 02_student_scores.py      # API → Average → Matplotlib
│   ├── 03_csv_to_sqlite.py       # CSV → SQLite (users)
│   ├── books.db                  # Generated SQLite DB (gitignored)
│   ├── users.db                  # Generated SQLite DB (gitignored)
│   ├── student_scores.png        # Generated chart
│   ├── requirements.txt
    ├── sample_data/
│   |   └── users.csv              # 26 sample user records
│   └── README.md
├── problem_statement_2/          # Theory / research
│   ├── llm_chatbot_architecture.md   # Chatbot architecture + diagram
│   ├── vector_database_analysis.md   # Vector DB analysis + selection
│   ├── self_assessment.md            # A/B/C rating (LLM, DL, AI, ML)
│   └── diagrams/                     # Architecture diagrams
├── screenshots/
│   └── student_scores.png
├── .gitignore
└── README.md
```

---

## Problem Statement 1 — Quick Start

All scripts resolve paths relative to their own file location (`Path(__file__).resolve().parent`), so they work from any working directory.

```bash
# From repository root or from problem_statement_1/
pip install -r problem_statement_1/requirements.txt

# Run each task
python3 problem_statement_1/01_api_to_sqlite.py   # → creates problem_statement_1/books.db
python3 problem_statement_1/02_student_scores.py  # → creates problem_statement_1/student_scores.png
python3 problem_statement_1/03_csv_to_sqlite.py   # → creates problem_statement_1/users.db

# Or from inside the folder
cd problem_statement_1
python3 01_api_to_sqlite.py
python3 02_student_scores.py
python3 03_csv_to_sqlite.py
```

| Task | Script | Input | Output | Technique |
|------|--------|-------|--------|-----------|
| API → SQLite (books) | `01_api_to_sqlite.py` | Open Library API `search.json?q=python` | `books.db` (10 books) | `requests`, `sqlite3`, `INSERT OR IGNORE` |
| Scores → Avg → Chart | `02_student_scores.py` | jsonplaceholder `/users` (+ synthetic scores) | `student_scores.png` + avg | `requests`, `matplotlib`, `axhline` |
| CSV → SQLite | `03_csv_to_sqlite.py` | `sample_data/users.csv` | `users.db` (25 users) | `csv.DictReader`, `sqlite3` |

See `problem_statement_1/README.md` for detailed data flows, assumptions, and error handling.

---

## Problem Statement 2 — Theory

| Document | Content |
|----------|---------|
| `problem_statement_2/llm_chatbot_architecture.md` | High-level LLM chatbot architecture: 10 components (Client, API Gateway, Auth, Conversation Manager, RAG/Retrieval, Vector DB, Prompt Builder, LLM, Guardrails, Observability) + end-to-end build steps. Includes ASCII architecture diagram. |
| `problem_statement_2/vector_database_analysis.md` | Vector database deep dive: embedding, similarity metrics (cosine/euclidean/dot), indexing (HNSW/IVF/PQ/ANN), metadata filtering, hybrid search, 5-way comparison (FAISS, pgvector, Pinecone, Weaviate, Milvus), and selection (Weaviate for enterprise RAG, pgvector as alternative). |
| `problem_statement_2/self_assessment.md` | Self-rating A/B/C for LLM, Deep Learning, AI, ML with justifications and evidence (see scale: A = independent, B = under supervision, C = little/no understanding). |
| `problem_statement_2/diagrams/` | Exported architecture diagrams (PNG) referenced by the docs. |

---

## Most Complex Code — Links

As requested in Problem Statement 1:

### Most Complex Python Code

1. **Research Verification Agent (5-Agent LangGraph)** — Orchestrator, Research, Analyst, Writer, Fact-Checker agents with LangGraph `StateGraph`, Groq model tiering, and automated report generation.
   - **Link:** <https://github.com/02tanishq/Research-Verification-Agent>

2. **ResearchRAG** - An autonomous AI Research Report Generator featuring multi-stage RAG, FAISS vector search, Cross-Encoder reranking, contradiction detection, and citation provenance verification across academic PDF literature.
   - **Link** <https://github.com/02tanishq/ResearchRAG>

### Most Complex Database Code

1. **Enterprise Data Warehouse (3-Tier Medallion & Star Schema)** — End-to-end T-SQL ETL pipeline and dimensional model (1 fact, 3 dimension tables) integrating 18K+ CRM and 60K+ ERP transactions with surrogate key validation for KPI analytics.
   -**Link** <https://github.com/02tanishq/Enterprise-Data-Warehousel-/tree/main>

All repositories are public unless noted. Private repos available on request.

---

## Technologies

Python, REST API, JSON, SQLite, SQL, CSV, Matplotlib, Requests, Vector Databases, RAG, LLM, Pathlib


---

## Notes

- Assumptions are documented inline and in `problem_statement_1/README.md` and `problem_statement_2/vector_database_analysis.md`.
- Databases (`*.db`) and generated images are gitignored; they are recreated by running the scripts.
- Scripts handle missing fields, empty responses, duplicate records (`INSERT OR IGNORE`), and use timeouts on API calls.
