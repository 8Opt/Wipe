import os 
from dotenv import load_dotenv

load_dotenv()

def setup_api_key(): 
    os.environ['TAVILY_API_KEY'] = os.getenv('TAVILY_API_KEY')
    os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
    os.environ['GOOGLE_API_KEY'] = os.getenv('GEMINI_API_KEY')
