from configparser import ConfigParser


class config:
    def __init__(self, config_file_path="src/Langgraphagenticai/ui/stremlitui/uiconfigfile.ini"):
        self.config_file_path = config_file_path
        self.config = ConfigParser()
        self.config.read(self.config_file_path)

    def get_llm_options(self):
        return self.config.get("DEFAULT", "LLM_OPTIONS").split(",")
    
    def get_usecase_options(self):
        return self.config.get("DEFAULT", "USECASE_OPTIONS").split(",")
    
    def get_groq_model_options(self):
        return self.config.get("DEFAULT", "GROQ_MODEL_OPTIONS").split(",")
    
    def get_page_title(self):
        return self.config.get("DEFAULT", "PAGE_TITLE")
    
    