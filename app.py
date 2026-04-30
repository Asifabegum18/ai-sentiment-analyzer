import streamlit as st
from Sentiment import analyze_sentiment

# Page settings
st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🧠",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #4A90E2;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">💬 AI Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze emotions from text using NLP</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📌 About Project")
st.sidebar.info(
    """
    This AI project uses:
    
    - Python
    - TextBlob
    - Streamlit
    - Natural Language Processing (NLP)
    
    Developed for AI & Data Science portfolio.
    """
)

# Input box
text = st.text_area("✍️ Enter your text below:", height=150)

# Analyze button
if st.button("🔍 Analyze Sentiment"):

    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        sentiment, polarity, subjectivity = analyze_sentiment(text)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)

        st.subheader("📊 Analysis Result")

        # Sentiment
        if "Positive" in sentiment:
            st.success(f"Sentiment: {sentiment}")
        elif "Negative" in sentiment:
            st.error(f"Sentiment: {sentiment}")
        else:
            st.warning(f"Sentiment: {sentiment}")

        # Scores
        st.write(f"### Polarity Score: `{polarity:.2f}`")
        st.progress(min(abs(polarity), 1.0))

        st.write(f"### Subjectivity Score: `{subjectivity:.2f}`")

        # Meaning
        st.info("""
        **Polarity**
        -1 → Negative  
         0 → Neutral  
        +1 → Positive

        **Subjectivity**
        0 → Fact-based  
        1 → Opinion-based
        """)

        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("🚀 Built with Streamlit & TextBlob")