import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv(dotenv_path="data/keys.env")

llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0,
    max_retries=2,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Page setup
st.set_page_config(page_title="CareerLens Assistant", page_icon="💼")
st.markdown(
    """
    <div style='text-align: center; padding: 10px; margin-bottom : 30px; background: linear-gradient(135deg, #f4eaff, #e9dfff); border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
        <h1 style='font-family: "Segoe UI", sans-serif; color: #2c3e50;'>
            💬 CareerLens Chat Assistant
        </h1>
        <p style='font-size: 16px; color: #34495e;'>
            Your AI companion for resume tips, job advice, and career strategy ✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize history
# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chatbox at bottom!
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    response = llm.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=response.content))

# Show empty chat image *after* handling input
if len(st.session_state.chat_history) == 0:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image(
            "assets/empty_chat.png",
            caption="Start the conversation and CareerLens will guide you!",
            use_container_width=True,
            width=100
        )

# Display chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    else:
        with st.chat_message("assistant"):
            st.markdown(msg.content)