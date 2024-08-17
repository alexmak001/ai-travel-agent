from textwrap import dedent
from phi.assistant import Assistant
from phi.tools.serpapi_tools import SerpApiTools
import streamlit as st
from phi.llm.openai import OpenAIChat
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_KEY_SECRET")

st.title("Trip Planner")

researcher = Assistant(llm=OpenAIChat(model="gpt-4o-mini-2024-07-18"),
                       tools=[SerpApiTools(api_key=os.getenv("API_KEY_SERPAPI"))])

st.write(researcher.run("Whats happening in Amsterdam?",markdown=True, stream=True))

# planner = Assistant("gpt-4o", openai_api_key)
