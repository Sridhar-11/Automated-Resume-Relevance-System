from fuzzywuzzy import fuzz
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def hard_match(resume_text, skills_list):
    resume_text_lower = resume_text.lower()
    score = 0
    missing_skills = []
    for skill in skills_list:
        if fuzz.partial_ratio(skill.lower(), resume_text_lower) > 80:
            score += 1
        else:
            missing_skills.append(skill)
    hard_score = (score / len(skills_list)) * 100
    return hard_score, missing_skills

def semantic_match(resume_text, jd_text):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    similarity = util.cos_sim(resume_embedding, jd_embedding).item()
    semantic_score = similarity * 100
    return semantic_score

def final_score(hard_score, semantic_score, hard_weight=0.6, soft_weight=0.4):
    score = (hard_score * hard_weight) + (semantic_score * soft_weight)
    if score >= 80:
        verdict = "High Fit"
    elif score >= 60:
        verdict = "Medium Fit"
    else:
        verdict = "Low Fit"
    return score, verdict

def evaluate_resume(resume_text, jd_text, skills_list):
    hard_score, missing_skills = hard_match(resume_text, skills_list)
    semantic_score = semantic_match(resume_text, jd_text)
    score, verdict = final_score(hard_score, semantic_score)
    return {
        "Relevance Score": round(score, 2),
        "Verdict": verdict,
        "Missing Skills": missing_skills
    }
