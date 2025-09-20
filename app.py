import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from jd_parser import extract_jd_text
from evaluator import evaluate_resume

skills = ["Python", "SQL", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Power BI", "BeautifulSoup", "Scikit-learn"]

st.title("Automated Resume Relevance Check System")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
jd_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

if st.button("Evaluate") and resume_file and jd_file:
    # Save temporary files
    with open("temp_resume", "wb") as f:
        f.write(resume_file.getbuffer())
    with open("temp_jd.txt", "wb") as f:
        f.write(jd_file.getbuffer())
    
    if resume_file.type == "application/pdf":
        resume_text = extract_text_from_pdf("temp_resume")
    else:
        resume_text = extract_text_from_docx("temp_resume")
    
    jd_text = extract_jd_text("temp_jd.txt")
    
    result = evaluate_resume(resume_text, jd_text, skills)
    
    st.subheader("Evaluation Result")
    st.json(result)
