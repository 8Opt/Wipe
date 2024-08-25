import os 

class GenModel: 
    
    @staticmethod
    def from_pretrained(provider, config): 
        try: 
            match provider:
                case    'gemini': 
                    try:
                        from langchain_google_genai import ChatGoogleGenerativeAI
                        return ChatGoogleGenerativeAI(**config)
                    except ImportError as e: 
                        raise e

                case    "ollama": 
                    try:
                        from langchain_community.chat_models import ChatOllama
                        return ChatOllama(**config)
                    except ImportError as e: 
                        raise e

                case    "groq": 
                    try:
                        from langchain_groq import ChatGroq
                        return ChatGroq(**config)
                    except ImportError as e: 
                        raise e

                case    "openai": 
                    try:
                        from langchain_openai import ChatOpenAI
                        return ChatOpenAI(**config)
                    except ImportError as e: 
                        raise e

        except ValueError:
            raise ValueError("Please input valid provider!")
