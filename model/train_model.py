import pandas as pd
import re
import string
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

print("Training script started...")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

data_path = os.path.join(BASE_DIR, "dataset", "resume_data.csv")

print("Loading dataset from:", data_path)

df = pd.read_csv(data_path)

print("Dataset loaded successfully")
print("Total rows:", len(df))

# Fix hidden column name
df.rename(columns={'﻿job_position_name': 'job_position_name'}, inplace=True)

# Combine text fields
df["resume_text"] = (
    df["career_objective"].fillna("") + " " +
    df["skills"].fillna("") + " " +
    df["responsibilities"].fillna("")
)

df = df[["resume_text", "job_position_name"]].dropna()

print("Preparing text...")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

df["resume_text"] = df["resume_text"].apply(clean_text)

# Encode labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df["job_position_name"])

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    df["resume_text"],
    y,
    test_size=0.2,
    random_state=42
)

print("Vectorizing text...")

vectorizer = TfidfVectorizer(max_features=2000, stop_words="english")

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("Training model...")

model = LogisticRegression(max_iter=300)

model.fit(X_train_vec, y_train)

pred = model.predict(X_test_vec)

acc = accuracy_score(y_test, pred)

print("Model Accuracy:", acc)

# Save models
model_path = os.path.join(BASE_DIR, "model", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "model", "vectorizer.pkl")
encoder_path = os.path.join(BASE_DIR, "model", "label_encoder.pkl")

pickle.dump(model, open(model_path, "wb"))
pickle.dump(vectorizer, open(vectorizer_path, "wb"))
pickle.dump(label_encoder, open(encoder_path, "wb"))

print("Model saved successfully!")