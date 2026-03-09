import re
from skill_extraction.skills_database import skills_list

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern,text):
            found_skills.append(skill)

    return found_skills