import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def classify_email(email_text):
    prompt = f"""Classify this email into:
- Support
- Billing
- Feedback
- Internal
- Spam

Email: "{email_text}"
Just return the category."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

def summarize_email(email_text):
    prompt = f"""Summarize this email in 2 short bullet points:
Email: "{email_text}" """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

def draft_reply(email_text):
    prompt = f"""Generate a professional, polite reply to this email:
Email: "{email_text}" """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

# Streamlit UI
st.title("📧 AI Email Assistant")

email_input = st.text_area("Paste your email here:", height=200)

if st.button("Analyze Email"):
    if email_input:
        with st.spinner("Thinking..."):
            category = classify_email(email_input)
            summary = summarize_email(email_input)
            reply = draft_reply(email_input)

        st.success("Done!")
        st.subheader("📂 Category:")
        st.write(category)

        st.subheader("📝 Summary:")
        st.write(summary)

        st.subheader("📬 Suggested Reply:")
        st.write(reply)
    else:
        st.warning("Please paste an email above.")
