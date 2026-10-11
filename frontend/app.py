
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/summarize/"

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("AI Text Summarizer")
st.write("Summarize long text using your local Llama 3.2 AI model.")

text = st.text_area(
    "Enter the text you want to summarize:",
    height=250,
    placeholder="Paste an article, paragraph, or notes here..."
)

if st.button("Summarize Text", type="primary"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Generating your summary..."):
            try:
                response = requests.post(
                    API_URL,
                    data={"text": text},
                    timeout=180
                )
                response.raise_for_status()
                result = response.json()

                st.subheader("Your Summary")
                st.write(result["summary"])

            except requests.RequestException:
                st.error(
                    "Could not connect to the backend. "
                    "Make sure the FastAPI server is running."
                )

st.caption("Powered by Streamlit, FastAPI, Ollama, and Llama 3.2")
