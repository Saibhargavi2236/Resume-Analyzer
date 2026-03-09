import pickle
import os
from model.role_mapping import role_mapping
BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))
label_encoder = pickle.load(open(os.path.join(BASE_DIR, "label_encoder.pkl"), "rb"))

def predict_role(text):

    text_vec = vectorizer.transform([text])

    pred = model.predict(text_vec)

    role = label_encoder.inverse_transform(pred)[0]

    # Map role if available
    mapped_role = role_mapping.get(role, role)

    return mapped_role