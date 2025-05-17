import streamlit as st
import openai

st.title("📘 Sinhala AI Note Summarizer")
st.write("Paste your Sinhala text below and click 'Summarize'.")

openai.api_key = st.secrets["openai_api_key"]

text_input = st.text_area("✏️ Paste Sinhala text here:")

if st.button("🔁 Summarize"):
    if text_input:
        with st.spinner("Summarizing..."):
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a Sinhala language assistant. Summarize the following paragraph into 3-5 sentences suitable for Sri Lankan A/L students."},
                    {"role": "user", "content": text_input}
                ],
                temperature=0.5
            )
            summary = response['choices'][0]['message']['content']
            st.success("✅ Summary:")
            st.write(summary)
    else:
        st.warning("Please enter some text first.")
