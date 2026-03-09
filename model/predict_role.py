import pickle
import os
import numpy as np

BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR,"model.pkl"),"rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR,"vectorizer.pkl"),"rb"))
label_encoder = pickle.load(open(os.path.join(BASE_DIR,"label_encoder.pkl"),"rb"))

def predict_top_roles(text):

    text_vec = vectorizer.transform([text])

    probs = model.predict_proba(text_vec)[0]

    top_indices = np.argsort(probs)[::-1][:3]

    roles = label_encoder.inverse_transform(top_indices)

    results = []

    for role, index in zip(roles, top_indices):
        confidence = round(probs[index] * 100, 2)
        results.append((role, confidence))

    return results
