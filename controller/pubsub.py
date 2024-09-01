"""
    Defines Pub/Sub logic for the AI news update feature.
"""
from wipe.wipe_producer import WipeProducer
from wipe.wipe_customer import WIPEConsumer
from wipe.wipe_redis import WIPEDB
from wipe.helpers import read_yaml, str_to_json, json_to_str, set_logger

from controller.news_features import get_latest_trend

config =  read_yaml('./config.yaml')
logger = set_logger()

producer = WipeProducer(topic_name=config["pubsub"]["topic"],
                            partition=config["pubsub"]["partition"])
consumer = WIPEConsumer(topic_name=config["pubsub"]["topic"],
                            partition=config["pubsub"]["partition"])
wipe_db = WIPEDB(db_config=config['wipe_db'])

# ===== PRODUCER'S METHODS =====
def pub_produce_articles():
    """
    Publishes summarized articles to the defined topic.
    """
    logger.info("[PRODUCER]: Start catching trends")
    trends = get_latest_trend() #   (articles, events)
    for article, event in zip(trends[0], trends[1]):

        logger.info("[PRODUCER]: Send event to consumers")
        event_str = json_to_str(event.json())
        producer.produce_records(event_str)  # Serialize event to JSON

        logger.info("[PRODUCER]: Set Article object to Database.")
        article_str = json_to_str(article.json())
        wipe_db.set_article(id=article.id, 
                            role=producer.ROLE, 
                            content=article_str)
    producer.flush()


# ===== CONSUMER'S METHODS =====
def sub_catch_articles():
    """
    Consumes events from the topic and processes them (implementation pending).
    """
    logger.info("[CONSUMER]: Catch events from Producer")
    consumer.consume_records(config["pubsub"]["num_records_consume"])

def sub_read_articles(): 
    """
    Retrieve articles from the database based on the events.
    Note: 
        Assume the Consumer chose the 1-latest event. 
    """

    logger.info("[CONSUMER]: Get event")
    event = consumer.notification[-1]

    while not isinstance(event, dict):
        event = str_to_json(event)

    logger.info("[CONSUMER]: Get article")
    article_id = event['article_id']
    article = wipe_db.get_article(id=article_id, 
                                  role=consumer.ROLE)

    logger.info(f"[CONSUMER]: Reading\n{article}")

