import streamlit as st
import PyPDF2
import pyttsx3
import tempfile

st.title("PDF to Audio Converter")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    full_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            full_text += text
    if not full_text.strip():
        st.warning("No extractable text was found in your PDF.")
    else:
        st.text_area("Extracted Text", full_text[:2000])  # Preview first 2000 chars

        # Convert text to audio
        engine = pyttsx3.init()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            engine.save_to_file(full_text, f.name)
            engine.runAndWait()
            st.audio(f.name)
            st.success("Conversion completed! Listen above.")

