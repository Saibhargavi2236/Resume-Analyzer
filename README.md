# Resume-Analyzer
# AI Resume Analyzer

An AI-powered Resume Analyzer that automatically analyzes resumes using Machine Learning and Natural Language Processing (NLP).  
The system predicts the most suitable job role, extracts skills, identifies skill gaps, and calculates an ATS (Applicant Tracking System) score.

---

## 🚀 Features

✔ Resume text extraction from PDF  
✔ Job role prediction using Machine Learning  
✔ Skill extraction from resume  
✔ Skill gap analysis  
✔ ATS score calculation  
✔ Suggests missing skills

---

## 🧠 Machine Learning Models Used

The system was trained and evaluated using multiple models:

- Logistic Regression
- Support Vector Machine (SVM)
- Naive Bayes
- Random Forest
- Decision Tree

Final model uses **TF-IDF + Logistic Regression** for high accuracy.

---

## 🛠 Tech Stack

**Programming Language**
- Python

**Libraries**
- Scikit-learn
- Pandas
- NumPy
- PDFPlumber
- Regex (re)

**Machine Learning**
- TF-IDF Vectorization
- Logistic Regression
- Label Encoding

---

## 📂 Project Structure
Resume-Analyzer
│
├── dataset
│ └── resume_data.csv
│
├── model
│ ├── train_model.py
│ ├── predict_role.py
│ ├── model.pkl
│ ├── vectorizer.pkl
│ └── label_encoder.pkl
│
├── resume_parser
│ └── extract_text.py
│
├── skill_extraction
│ ├── skill_extractor.py
│ └── skills_database.py
│
├── ats_scoring
│ ├── skill_gap_analysis.py
│ └── ats_score.py
│
├── uploads
│ └── resume.pdf
│
└── notebook
└── resume_analyzer.ipynb

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Resume-Analyzer.git
cd Resume-Analyzer
Install required packages:

pip install -r requirements.txt
▶️ How to Run the Project
Train the model:

python model/train_model.py
Run the analyzer in Jupyter Notebook:

jupyter notebook
Open:

resume_analyzer.ipynb
## 📊 Example Output
Predicted Role: Full Stack Developer

Extracted Skills:
['html','css','javascript','react','nodejs','mongodb','aws']

Matched Skills:
['html','css','javascript','react','nodejs']

Missing Skills:
['docker']

ATS Score:
85%
## 🔄 System Workflow
Resume Upload
      ↓
Text Extraction
      ↓
Resume Text Cleaning
      ↓
TF‑IDF Vectorization
      ↓
Machine Learning Model
      ↓
Job Role Prediction
      ↓
Skill Extraction
      ↓
Skill Gap Analysis
      ↓
ATS Score Calculation

## 📌 Future Improvements
Resume improvement suggestions

Automatic job description matching

Web dashboard interface

Top‑3 job role predictions

Deep learning models

