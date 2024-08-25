from controller.setup_env import setup_api_key, get_config

from wipe.llms import GenModel
from wipe.pre_processing import clean
from wipe.prompts import SUMMARY_ARTICLE
from wipe.tools import SmartScraper, TavilySearcher
from wipe.elements.schema import Article

setup_api_key()

config = get_config()
scraper = SmartScraper()
searcher = TavilySearcher(config=config['search'])
llm = GenModel.from_pretrained(provider='gemini', 
                               config=config['summarizer']['llm'])


trend = "What is the latest trend in AI 2024?"

def get_latest_trend()->list[Article]: 
    """Getting latest trend in AI field via predefined-prompt.

    Returns:
        list[Article]: List of `Article` object
    """
    urls = []
    related_ans = searcher.run(trend)
    for result in related_ans['results']: 
        urls.append(result['url'])

    # There are several website that can not be scraped via LangChain supported method, therefore, I filter it out.
    docs = []
    for url in urls: 
        try: 
            doc = scraper.run(url)
            docs.append(doc)
        except: 
            continue

    articles = []
    for idx in range(len(docs)): 
        doc = docs[idx][0]
        
        metadata = doc.metadata
        content = doc.page_content
        content = clean(content)

        summary_prompt = SUMMARY_ARTICLE.format(article=content)

        summary = llm.invoke(summary_prompt).content

        article = Article(title=metadata['title'], 
                          abstract=metadata['description'], 
                          summary=summary, 
                          url=metadata['source'])
        
        articles.append(article)
        
    return articles