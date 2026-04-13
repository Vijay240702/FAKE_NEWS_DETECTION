import streamlit as st
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_news(text):
    vector = vectorizer.transform([text])
    return model.predict(vector)[0]

st.title("Fake News Detection App")

input_text = st.text_area("Enter News Text")

if st.button("Check"):
    result = predict_news(input_text)
    
    if result == "FAKE":
        st.error("This News is FAKE ❌")
    else:
        st.success("This News is REAL ✅")
        
