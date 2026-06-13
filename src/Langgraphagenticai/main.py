import streamlit as st

from src.langgraphagenticai.ui.uiconfigfile import LoadStreamlitUI

def load_langgraph_agenticai_app():

    """ Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness. It also provides a sidebar for user controls and configuration options.
    """

    ##Load UI
    ui= LoadStreamlitUI()
    user_input= ui.load.streamlit_ui()

    if not user_input:
        st.error("Error: User input is not available. Please check the UI configuration.")
        return
    
    user_message = st.chat_input("Enter your message here...")