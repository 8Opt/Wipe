"""
    Define logic for update AI news feature.
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables (assuming .env file exists)
load_dotenv()

# Project Root Directory
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]

# Ensure project root is in sys.path
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# Relative path to project root
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))


# Import necessary modules
from controller.setup_env import setup_api_key, get_config
from wipe.llms import GenModel
from wipe.pre_processing import clean
from wipe.prompts import SUMMARY_ARTICLE
from wipe.tools import SmartScraper, TavilySearcher
from wipe.elements.schema import Article, Event

# Setup API key and configuration
setup_api_key()
config = get_config()

# Initialize tools
scraper = SmartScraper()
searcher = TavilySearcher(config=config["search"])
llm = GenModel.from_pretrained(
    provider=config["summarizer"]["provider"], config=config["summarizer"]["llm"]
)

TREND = "What is the latest trend in AI 2024?"

def get_latest_trend() -> tuple[list[Article], list[Event]]:
    """
    Retrieves the latest trend in AI and returns a list of summarized articles.

    Returns:
        list[Article]: A list of Article objects containing summaries of relevant news.
    """

    # Find relevant URLs
    urls = [result["url"] for result in searcher.run(TREND)["results"]]

    # Filter out unsupported URLs and scrape content
    docs = []
    for url in urls:
        try:
            docs.append(scraper.run(url))
        except ValueError:
            pass  # Skip unsupported URLs


    # Process and summarize articles
    articles, events = [], []
    for idx, doc in enumerate(docs):
        metadata = doc[0].metadata
        content = clean(doc[0].page_content)

        summary_prompt = SUMMARY_ARTICLE.format(article=content)
        summary = llm.invoke(summary_prompt).content

        # Create Article object with metadata and summary
        article = Article(summary=summary, **metadata)
        articles.append(article)
        # Create Event object with Article's information
        event_title = f"Latest Trend in AI (2024) - {article.title}"  # Modify title creation if needed
        event = Event(title=event_title, 
                      article_id=article.id)
        events.append(event)
    return (articles, events)