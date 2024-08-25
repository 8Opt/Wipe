from typing import List, Union


from langchain_community.document_loaders import WebBaseLoader


from wipe.tools.base import Node


class SmartScraper(Node): 

    def __init__(self, name="SmartScraper",**kwargs):
        super().__init__(name=name,  **kwargs)

    def run(self, input, **kwargs):
        loader = self.__get_web_loader(url=input)
        result = loader.load()
        return result

    def __get_web_loader(self, url: Union[str, List[str]]): 
        loader = WebBaseLoader(url)
        return loader
