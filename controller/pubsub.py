"""
    Defines Pub/Sub logic for the AI news update feature.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Project Root Directory
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]

# Ensure project root is in sys.path
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# Relative path to project root
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))

from wipe.wipe_producer import WipeProducer
from wipe.wipe_customer import WIPEConsumer
from wipe.wipe_redis import WIPEDB
from wipe.helpers import read_yaml, str_to_json, json_to_str

from controller.news_features import get_latest_trend

config =  read_yaml('./config.yaml')
producer = WipeProducer(topic_name=config["pubsub"]["topic"],
                            partition=config["pubsub"]["partition"])
consumer = WIPEConsumer(topic_name=config["pubsub"]["topic"],
                            partition=config["pubsub"]["partition"])
wipe_db = WIPEDB(db_config=config['wipe_db'])

def pub_produce_articles():
    """
    Publishes summarized articles to the defined topic.
    """
    articles, events = get_latest_trend()
    for event in events:
        producer.produce_records(event.json())  # Serialize event to JSON
    producer.flush()


def sub_consume_articles():
    """
    Consumes events from the topic and processes them (implementation pending).
    """
    consumer.consume_records(config["pubsub"]["num_records_consume"])