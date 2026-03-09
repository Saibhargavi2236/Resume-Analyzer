from app import analyze_resume

required_skills = ["python","machine learning","sql","aws"]

result = analyze_resume("uploads/resume.pdf",required_skills)

print(result)