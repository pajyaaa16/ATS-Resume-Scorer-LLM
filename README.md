# 📄 ATS Resume Scorer — LLM Powered

An **LLM-based Applicant Tracking System (ATS)** that evaluates resumes against job descriptions using a real Large Language Model.  
Built with **Python, Streamlit, and Groq (LLaMA-3.1)** to simulate modern AI-powered recruitment systems.


## 🔥 Key Highlights 

- ✅ Uses **real LLM API** (Groq – LLaMA-3.1)
- ✅ Semantic resume–JD comparison (not keyword-only)
- ✅ ATS Score (0–100)
- ✅ Skill gap detection
- ✅ Actionable improvement suggestions
- ✅ Clean, modern Streamlit UI
- ✅ Free & production-style API integration

---

## 🧠 What Problem This Solves

Traditional ATS systems rely heavily on keyword matching, leading to:
- False rejections
- Poor skill understanding
- Low candidate experience

This project uses **LLM-based semantic analysis** to:
- Understand context, not just keywords
- Match resumes more intelligently
- Provide human-like feedback automatically

---

## 🛠️ Tech Stack

### Frontend
- **Streamlit** – Interactive web UI

### Backend / AI
- **Python 3.10+**
- **Groq API** (Free Tier)
- **LLaMA-3.1 (8B Instant)**
- **pdfplumber** – PDF resume text extraction
- **python-dotenv** – Secure API key management

---
## 🧩 System Architecture
User
│
│ Upload Resume + Job Description
▼
Streamlit UI
│
▼
PDF Text Extraction (pdfplumber)
│
▼
LLM Prompt Engineering
│
▼
Groq LLaMA-3.1 API
│
▼
ATS Score + Insights

---

## 📊 Output Example
ATS Score: 78 / 100

Missing Skills:

Docker

AWS

REST APIs

Strengths:

Strong Python and Machine Learning background

Relevant project experience in NLP

Improvement Suggestions:

Add cloud-related tools

Quantify project outcomes

---
🔑 API Details

Provider: Groq

Model: LLaMA-3.1-8B-Instant

Type: Chat Completion API

Cost: Free tier (no credit card)

Used for:

Resume–JD semantic evaluation

Skill gap analysis

ATS scoring

Improvement recommendations

🗄️ Database Design

🚫 No database required (stateless design)

Reason:

Resume analysis is real-time

No persistent storage needed

🔮 Future Enhancements

Hybrid scoring (ML + LLM)

Resume comparison dashboard

PDF report download

User authentication

Database-backed analytics

👨‍💻 Author

Prajwal Kindre
B.E. Artificial Intelligence & Data Science

📌 Interests: Backend Development • AI/ML • NLP • LLMs

⭐ Final Note for Recruiters

This project reflects my ability to:

Integrate real-world AI APIs

Design scalable AI systems

Build clean UI-driven applications

Solve practical industry problems using LLMs