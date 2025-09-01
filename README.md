# 💀 KingSh*t's Punchlines 💀
KingSh*t's Punchlines is an interactive web application that serves as a dark-humor chatbot. Powered by Google's Gemini LLM and built with Streamlit and LangChain, this app delivers short, cynical, and witty punchlines in response to user prompts.

The AI persona, "KingSh*t," is designed to be arrogant and unapologetically grim, ensuring every interaction is a foray into the darker side of comedy.

# ✨ Features
Interactive Chat Interface: A simple and clean UI built with Streamlit.

AI-Powered Persona: Features "KingSh*t," a cynical AI comedian with a dark sense of humor.

Punchline Focused: The AI is instructed to only provide short, sharp punchlines, no filler.

Dark Humor: All content is generated with a dark, cynical, and edgy style.

Conversation Reset: Easily start a new conversation with a single click.

Powered by Google Gemini: Utilizes the gemini-1.5-flash model for fast and creative responses.

# 🛠️ Tech Stack
Language: Python

Framework: Streamlit

AI Integration: LangChain

LLM: Google Gemini API

Configuration: python-dotenv

# 🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites

Python 3.8 or newer

A Google API Key with the Gemini API enabled. You can obtain one from Google AI Studio.

Installation



 Create and activate a virtual environment (recommended):

# For Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

# For macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```


Install the required dependencies:
The project dependencies are listed in requirements.txt. Install them using pip:
```bash

pip install -r requirements.txt
```

Set up your environment variables:

Create a new file named .env in the root directory of the project.

Add your Google API Key to this file:
```bash

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

Replace "YOUR_API_KEY_HERE" with your actual key.

Running the Application

Once the installation is complete, you can run the Streamlit app with the following command:
```bash
streamlit run chatbot.py
```

This will start a local web server, and you can view the application by navigating to the provided URL (usually http://localhost:8501) in your web browser.

# ✍️ How to Use
Open the web application in your browser.

Type a setup for a joke, a topic, or any phrase into the input box at the bottom.

Press Enter.

Watch as KingSh*t delivers a grim and witty punchline.

To start over, click the "Reset to Nothing" button in the sidebar.

