from tavily import TavilyClient

from wipe.tools.base import Node

class TavilyWorker(Node):
    def __init__(self, api_key:str,name="Tavily"):
        super().__init__(name=name,api_key=api_key)
        self.engine = TavilyClient(api_key=api_key)

    def run(self, input, search_type:str='basic', **kwargs): 
        
        try: 
            if search_type == "basic": 
                result = self.engine.search(query=input, 
                                            **kwargs)
            elif search_type == "context": 
                result = self.engine.get_search_context(query=input, 
                                            **kwargs)
            elif search_type == "qna": 
                result = self.engine.qna_search(query=input, 
                                            **kwargs)
            else: 
                supported_search = self._get_engine()
                supported_search = supported_search.keys()
                raise f"Input search_stype is not valid, please refer to {supported_search}"
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