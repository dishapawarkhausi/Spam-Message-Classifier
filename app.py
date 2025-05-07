import streamlit as st
import pickle
import numpy as np

# Load model and vectorizer
model = pickle.load(open("spam_classifier_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# App title
st.title("📩 Spam Message Classifier")

# Input box
user_input = st.text_area("Enter a message to check:")

# Predict on input
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Vectorize input
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        probability = model.predict_proba(input_vector)[0]

        # Display result
        if prediction == 1:
            st.error(f"⚠️ This message is **SPAM**.")
            st.write(f"Prediction confidence: `{probability[1]*100:.2f}%`")
        else:
            st.success(f"✅ This message is **HAM** (not spam).")
            st.write(f"Prediction confidence: `{probability[0]*100:.2f}%`")
