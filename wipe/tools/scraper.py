from langchain_community.document_loaders import WebBaseLoader

from wipe.tools.base import Node
from wipe.llms import GenModel

class SmartScraper(Node): 

    def __init__(self, api_key, **kwargs):
        super().__init__(api_key, name="SmartScraper",  **kwargs)
        if "llm_config" in kwargs: 
            self.llm_config = kwargs['llm_config']

    def run(self, input, **kwargs):
        return super().run(input, **kwargs)
    

    def __set_gen_model(self, provider, api_key): 
        try: 
            self.llm_config['api_key'] = api_key
            gen_model = GenModel.from_pretrained(provider=provider, 
                                                 config=self.llm_config)
            return gen_model
        
        except: 
            
