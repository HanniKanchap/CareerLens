import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

def resume_feedback(resume_text, expected, role):
    load_dotenv(dotenv_path="data/keys.env")
    llm = ChatGroq(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0,
        max_retries=2,
        groq_api_key=os.getenv('GROQ_API_KEY')
    )
    prompt = (
        f"Here is my resume content: {resume_text}\n"
        f"These are the expected skills: {expected}.\n"
        f"Suggest skills I should acquire and resources to use to improve ATS score for a {role} role. "
        f"Provide the output in bullet points."
    )
    response = llm.invoke(prompt)
    return response.text().strip().split('\n')