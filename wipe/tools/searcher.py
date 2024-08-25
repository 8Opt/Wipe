from tavily import TavilyClient

from wipe.tools.base import Node

class TavilySearcher(Node):
    def __init__(self, config, name="Tavily"):
        super().__init__(name=name)
        self.config = config
        self.engine = TavilyClient()

    def run(self, input, search_type:str='basic'): 
        
        try: 
            match search_type:
                case "basic": 
                    result = self.engine.search(query=input, 
                                                **self.config)
                    return result
                case "context": 
                    result = self.engine.get_search_context(query=input, 
                                                **self.config)
                    return result
                case "qna": 
                    result = self.engine.qna_search(query=input, 
                                                **self.config)
                    return result
        except: 
            return None
    
    def _get_engine(self): 
        supported_model = {
            "basic": """This tool offers two search depths:
                        Basic: Provides fast results, suitable for quick information needs.
                        Advanced: Delivers more thorough and high-quality results, but may take longer.
                        You can customize the search further using additional parameters (see documentation for details).
                        The results are returned as a JSON object containing all relevant information.""", 
            "context": "This tool simplifies web research by searching for relevant content and sources, then condensing it into a concise string within a specified token limit (defaulting to 4,000 tokens). It   eliminates the need for manual context extraction and token management, making it efficient for quickly gathering information from multiple web", 
            "qna": "This tool is designed to help AI agents find answers to questions. It searches the web, identifies the most relevant information, and returns a concise answer string along with supporting sources. By default, it uses an advanced search depth to ensure high-quality and accurate results."
        }
        return supported_model