import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analyzer 🧠")

text = st.text_input("Enter text")

if text:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        st.success("Positive 😊")
    elif polarity < 0:
        st.error("Negative 😡")
    else:
        st.warning("Neutral 😐")