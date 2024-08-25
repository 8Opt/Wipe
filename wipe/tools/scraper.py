from typing import List, Union


from langchain_community.document_loaders import WebBaseLoader


from wipe.tools.base import Node


class SmartScraper(Node): 

    def __init__(self, **kwargs):
        super().__init__(name="SmartScraper",  **kwargs)

    def run(self, input, **kwargs):
        results = self.__get_web_loader(url=input)
        return results

    def __get_web_loader(self, url: Union[str, List[str]]): 
        loader = WebBaseLoader(url)
        return loader
