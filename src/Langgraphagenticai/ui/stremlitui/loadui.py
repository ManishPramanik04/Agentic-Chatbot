import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import config

class LoadStreamlitUI:
    def __init__(self):
        self.config = config()
        self.user_controls={}
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖" + self.config.get_page_title())

        with st.sidebar:
            #Get options from config file
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            #LLM selection
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)

            if self.user_controls['selected_llm'] == "Groq":
                #Model Selection for Groq
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Groq Model", groq_model_options)
                self.user_controls['GROQ_API_KEY'] = st.session_state.get('GROQ_API_KEY', st.text_input("Enter Groq API Key", type="password"))

                #Validate API Key 
                if self.user_controls['GROQ_API_KEY']:
                    st.warning(" ☠️ Make sure to keep your API key secure and do not share it with anyone. Don't have? refer  : https://www.groq.com/docs/api-keys for more info.")         


            ##Use case selection
            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", usecase_options)        

     return self.user_controls  