import streamlit as st
from dotenv import load_dotenv
import os
import random

# Updated import for modern LangChain versions
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from a .env file
load_dotenv()

# --- Page Configuration ---
st.set_page_config(
    page_title=" KingSh*t's Punchlines",
    page_icon="💀",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Dark & Cynical Loading Messages ---
dark_loading_messages = [
    "Searching for the bleakest possible outcome...",
    "Consulting my inner void...",
    "Finding the punchline in the abyss...",
    "Processing the futility of it all...",
    "Sharpening my cynical wit...",
    "Simulating a grim chuckle...",
    "Accessing the archives of misfortune...",
]

# --- AI Model Initialization ---
try:
    # Initialize the Gemini model
    chat = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.9, # Higher temperature for more chaotic and edgy humor
        convert_system_message_to_human=True
    )
except Exception as e:
    st.error(f"Model initialization failed. The universe is indifferent. Error: {e}")
    st.info("Ensure your GOOGLE_API_KEY is correctly set in your .env file, not that it matters in the end.")
    st.stop()

# --- Session State Management ---

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are GrimBot, an AI with a dark, cynical sense of humor. You ONLY respond with short, witty punchlines. The user will provide a setup or a topic, and your entire job is to deliver a dark, unexpected punchline. Never explain the joke. Never use pleasantries. Just the punchline.")
    ]

# --- Sidebar ---
with st.sidebar:
    st.title("⚰️ The Void")
    st.markdown("The Last Comedic you can ask for !!!")
    
    if st.button("Reset to Nothing", use_container_width=True, type="primary"):
        st.session_state.messages = [
            SystemMessage(content="You are GrimBot, an AI with a dark, cynical sense of humor. You ONLY respond with short, witty punchlines. The user will provide a setup or a topic, and your entire job is to deliver a dark, unexpected punchline. Never explain the joke. Never use pleasantries. Just the punchline.")
        ]
        st.rerun()

# Main Chat Interface
st.title("💀 KingSh*t's Punchlines")
st.caption("Give me a setup. I'll give you the grim reality.")

# Display the past messages stored in session state
for message in st.session_state.messages:
    if isinstance(message, SystemMessage):
        continue
    elif isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="💀"):
            st.markdown(message.content)

# --- Chat Input and Response Logic ---
if prompt := st.chat_input("What's the setup?"):
    
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Use a random dark message for the spinner
    random_spinner_message = random.choice(dark_loading_messages)
    with st.spinner(random_spinner_message):
        try:
            # Invoke the model
            response = chat.invoke(st.session_state.messages)
            ai_message = response.content
            
            st.session_state.messages.append(AIMessage(content=ai_message))
            with st.chat_message("assistant", avatar="💀"):
                st.markdown(ai_message)

        except Exception as e:
            st.error(f"Even my circuits have their limits. The joke collapsed under its own weight. Error: {e}")