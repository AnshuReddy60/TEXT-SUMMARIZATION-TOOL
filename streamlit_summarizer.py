# streamlit_summarizer.py

import streamlit as st
from transformers import pipeline
import io

# ✅ Must be first Streamlit command
st.set_page_config(page_title="Text Summarizer - CodTech", layout="centered")

# Load summarization pipeline
@st.cache_resource
def load_summarizer():
    return pipeline("summarization")

summarizer = load_summarizer()

# App UI
st.title("📝 Text Summarization Tool")
st.write("Summarize lengthy articles using NLP techniques!")

# Input text area
text_input = st.text_area("📄 Paste your article here:", height=300)

# Summary length input field
st.markdown("### 🔢 Set Summary Length")
max_len = st.number_input("Enter maximum summary length (in tokens):", min_value=30, max_value=1024, value=200, step=10)
min_len = max(30, int(max_len * 0.5))  # Dynamic min based on max length

# Summarize button
if st.button("🔍 Summarize Now"):
    if len(text_input.split()) < 50:
        st.warning("⚠️ Please enter a longer article (at least 50 words).")
    else:
        with st.spinner("⏳ Summarizing..."):
            summary = summarizer(text_input, max_length=max_len, min_length=min_len, do_sample=False)
            st.success("✅ Summary generated!")
            st.markdown("### ✨ Summary:")
            st.write(summary[0]['summary_text'])

            # Prepare the summary for download
            summary_text = summary[0]['summary_text']
            byte_io = io.BytesIO()
            byte_io.write(summary_text.encode())  # Encode to bytes
            byte_io.seek(0)

            # Create download button
            st.download_button(
                label="Download Summary as .txt",
                data=byte_io,
                file_name="summary.txt",
                mime="text/plain"
            )

# Footer
st.markdown("---")
st.caption("🧠 Developed during CodTech Internship")
