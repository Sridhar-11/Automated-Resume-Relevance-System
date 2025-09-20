# Automated-Resume-Relevance-System
AI-powered Resume Relevance Check System for hackathon submission.

# Automated Resume Relevance Check System

## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Objective](#objective)
3. [Solution Approach](#solution-approach)
4. [Workflow](#workflow)
5. [Tech Stack](#tech-stack)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Project Structure](#project-structure)
9. [Demo](#demo)
10. [Contributors](#contributors)
11. [License](#license)

---

## Problem Statement
At Innomatics Research Labs, resume evaluation is currently manual, inconsistent, and time-consuming. Recruiters receive thousands of resumes per job posting, making it difficult to shortlist candidates quickly and accurately.  

**Challenge:** Build an automated system to evaluate resumes against job descriptions, generate relevance scores, and provide actionable feedback to students.

---

## Objective
- Automate resume evaluation at scale.  
- Generate a **Relevance Score (0–100)** per resume.  
- Highlight missing skills, certifications, and projects.  
- Provide a fit verdict: **High / Medium / Low suitability**.  
- Offer personalized improvement feedback to students.  
- Store results in a **web dashboard** accessible to recruiters.

---

## Solution Approach
Our system combines **rule-based checks** with **semantic AI analysis**:

1. **Resume & JD Parsing**  
   - Extract text from PDF/DOCX resumes and text-based job descriptions.  
2. **Hard Match (Keyword Matching)**  
   - Match skills, tools, and qualifications using exact/fuzzy matching.  
3. **Semantic Match (Contextual Understanding)**  
   - Convert resume and JD text into embeddings using **Sentence Transformers**.  
   - Compute cosine similarity to assess semantic fit.  
4. **Weighted Scoring & Verdict**  
   - Combine hard match (60%) and semantic match (40%) into final score.  
   - Verdict: High ≥80, Medium ≥60, Low <60.  
5. **Web Dashboard**  
   - Streamlit-based interface for recruiters to upload resumes & JDs.  
   - Displays relevance score, missing skills, and verdict instantly.

---

## Workflow
1. **Job Description Upload** → Upload JD file (`.txt`)  
2. **Resume Upload** → Upload resume file (`.pdf` / `.docx`)  
3. **Resume Parsing** → Extract text  
4. **Evaluation** → Hard match + semantic match + final scoring  
5. **Results** → Show Relevance Score, Verdict, and Missing Skills  
6. **Feedback** → Suggestions for student improvement  

---

## Tech Stack
- **Python Libraries:** pdfplumber, python-docx, pandas, numpy, scikit-learn, fuzzywuzzy, sentence-transformers, Streamlit  
- **Web App:** Streamlit (dashboard for recruiters)  
- **Embeddings & Semantic Search:** Sentence Transformers (`all-MiniLM-L6-v2`)  
- **Version Control & Sharing:** GitHub  

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/Automated-Resume-Relevance-System.git
cd Automated-Resume-Relevance-System
