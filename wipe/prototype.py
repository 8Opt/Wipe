from wipe.llms import GenModel
from wipe.pre_processing import clean
from wipe.prompts import SUMMARY_ARTICLE
from wipe.tools import SmartScraper, TavilySearcher


class WIPEContent(object): 

    def __init__(self, config, auto_clean:bool=True): 
        self.scraper = SmartScraper()
        self.searcher = TavilySearcher(config=config['search'])