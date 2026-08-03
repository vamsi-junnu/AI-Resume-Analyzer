def calculate_ats_score(skills):

    total_skills = 20

    score = (len(skills) / total_skills) * 100

    if score > 100:
        score = 100

    return round(score, 2)