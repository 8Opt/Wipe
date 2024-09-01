from wipe.prompts import PERSONA_PROMPT

class Provider:
  GEMINI = "gemini"
  OLLAMA = "ollama"
  GROQ = "groq"
  OPENAI = "openai"
  SAMBANOVA = "sambanova"  # Add Sambanova as a provider

class GenModel:

  PROVIDER_MAP = {
      Provider.GEMINI: "langchain_google_genai.ChatGoogleGenerativeAI",
      Provider.OLLAMA: "langchain_community.chat_models.ChatOllama",
      Provider.GROQ: "langchain_groq.ChatGroq",
      Provider.OPENAI: "langchain_openai.ChatOpenAI",
      Provider.SAMBANOVA: "SambaNova",  # Map to SambaNova class
  }

  @staticmethod
  def from_pretrained(provider, config):
    try:
      module_path, class_name = GenModel.PROVIDER_MAP[provider].rsplit(".", 1)
      module = __import__(module_path, fromlist=[class_name])
      return getattr(module, class_name)(**config)
    except (ImportError, KeyError) as e:
      raise ValueError(f"Invalid provider: {provider}") from e


class SambaNova:
  SAMBANOVA_API_URL = "https://fast-api.snova.ai/v1"
  SUPPORTED_MODEL = [
                    "Meta-Llama-3.1-8B-Instruct",          # CL-OL: 8192-1000
                    "Meta-Llama-3.1-70B-Instruct",         # CL-OL: 8192-1000
                    "Meta-Llama-3.1-405B-Instruct"         # CL-OL: 8192-1000
                     ]
  def __init__(self, api_key):
    try: 
        import openai
        self.client = openai.OpenAI(base_url=self.SAMBANOVA_API_URL, 
                                    api_key=api_key)
    except ImportError as ie:
        raise ImportError("`openai` is not installed. Please try `pip install openai`!") from ie
  
    self.SYS_PROMPT = PERSONA_PROMPT
    self.MODEL_NAME = "Meta-Llama-3.1-8B-Instruct"
    
  def invoke(self, prompt, **kwargs):
    completion = self.client.chat.completions.create(
      model=self.MODEL_NAME,
      messages=[{"role": "system", "content": self.SYS_PROMPT}, 
                {"role": "user", "content": prompt}],
      stream=True,
      **kwargs,
    )
    response = ""
    for chunk in completion:
      response += chunk.choices[0].delta.content or ""
    return response

    