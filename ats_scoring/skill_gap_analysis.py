def skill_gap(resume_skills, required_skills):

    resume_set = set(resume_skills)

    required_set = set(required_skills)

    matched = list(resume_set & required_set)

    missing = list(required_set - resume_set)

    return matched, missing