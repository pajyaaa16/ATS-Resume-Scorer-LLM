import streamlit as st
import pdfplumber
import os
from dotenv import load_dotenv
from groq import Groq
from docx import Document

# ---------------- ENV SETUP ----------------
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ATS Resume Scorer",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background-color: #0f172a;
}
h1, h2, h3 {
    color: #e5e7eb;
}
.stTextArea textarea {
    background-color: #020617;
    color: #e5e7eb;
}
.metric-box {
    background: linear-gradient(135deg, #6366f1, #22d3ee);
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
}
.card {
    background-color: #020617;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 20px;
    border: 1px solid #1e293b;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FILE TEXT EXTRACTION ----------------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_text_from_docx(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text.strip()

def extract_resume_text(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx") or file_name.endswith(".doc"):
        return extract_text_from_docx(uploaded_file)

    else:
        raise ValueError("Unsupported file format")

# ---------------- LLM RESPONSE ----------------
def get_llm_response(resume_text, job_description):
    prompt = """
You are an Applicant Tracking System (ATS).

Analyze the RESUME against the JOB DESCRIPTION and return output in EXACTLY this format:

ATS Score: <number between 0 and 100>

Missing Skills:
- skill1
- skill2

Strengths:
- strength1
- strength2

Improvement Suggestions:
- suggestion1
- suggestion2

Be concise, professional, and ATS-focused.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a professional ATS resume evaluator."},
            {
                "role": "user",
                "content": f"""
{prompt}

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}
"""
            }
        ],
        temperature=0.3,
        max_tokens=800
    )

    return response.choices[0].message.content

# ---------------- HEADER ----------------
st.markdown("## 📄 ATS Resume Scorer")
st.caption("✨ AI/ML Mini Project • LLM Powered • PDF & DOCX Supported")

st.divider()

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns([1.2, 1])

with col1:
    job_description = st.text_area(
        "📌 Job Description",
        height=220,
        placeholder="Paste job description here..."
    )

with col2:
    uploaded_file = st.file_uploader(
        "📤 Upload Resume (PDF / DOCX)",
        type=["pdf", "docx", "doc"]
    )

st.divider()

analyze_btn = st.button("🚀 Analyze Resume", use_container_width=True)

# ---------------- RESULT ----------------
if analyze_btn:
    if not uploaded_file or not job_description:
        st.warning("⚠️ Please upload a resume and provide job description.")
    else:
        with st.spinner("🧠 AI is evaluating the resume..."):
            resume_text = extract_resume_text(uploaded_file)
            result = get_llm_response(resume_text, job_description)

        # Extract score
        score = "N/A"
        for line in result.splitlines():
            if "ATS Score" in line:
                score = line.split(":")[-1].strip()
                break

        st.divider()
        st.markdown("## 📊 ATS Evaluation Result")

        colA, colB = st.columns([1, 2])

        with colA:
            st.markdown(
                f"<div class='metric-box'>ATS SCORE<br>{score}</div>",
                unsafe_allow_html=True
            )

        with colB:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 📋 Detailed Analysis")
            st.write(result)
            st.markdown("</div>", unsafe_allow_html=True)

