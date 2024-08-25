from controller.setup_env import setup_api_key

from wipe.llms import GenModel
from wipe.pre_processing import clean
from wipe.prompts import SUMMARY_ARTICLE
from wipe.tools import SmartScraper, TavilySearcher

setup_api_key()

prompt = "What is the latest trend in AI 2024?"

def get_latest_trend(config:dict): 
    scraper = SmartScraper()
    searcher = TavilySearcher(config=config['search'])