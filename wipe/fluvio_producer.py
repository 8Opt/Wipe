"""
A simple Fluvio producer that produces records to a topic.
"""

from datetime import datetime
from fluvio import Fluvio

from wipe.helpers import json_to_str
from wipe.wipe_redis import WIPEDB

class FluvioProducer:
    """
    A class to produce records to a Fluvio topic.
    
    Attributes:
    ----------
    topic_name : str
        The name of the topic to produce to.
    partition : int
        The partition to produce to.
    producer : Fluvio.topic_producer
        The Fluvio producer object.
        
    Methods:
    -------
    produce_records(num_records)
        Produces a specified number of records to the topic.
    flush()
        Flushes the producer to ensure all records are sent.
    """
    ROLE = "producer"
    def __init__(self, topic_name: str, partition: int, db_config:dict):
        """
        Initializes the FluvioProducer object.
        
        Parameters:
        ----------
        topic_name : str
            The name of the topic to produce to.
        partition : int
            The partition to produce to.
        """
        self.topic_name = topic_name
        self.partition = partition
        self.producer = Fluvio.connect().topic_producer(topic_name)
        self.db_connection = ...
        
    def produce_records(self, trends: tuple) -> None:
        """
        Produces a specified number of records to the topic.
        
        Parameters:
        ----------
        num_records : int
            The number of records to produce.
        """
        try:
            for article, event in zip(trends):
                event_str = json_to_str(event.dict())
                self.producer.send_string(event_str)
                
        except Exception as e:
            print(f"Error producing records: {e}")

    def flush(self) -> None:
        """
        Flushes the producer to ensure all records are sent.
        """
        try:
            self.producer.flush()
            print("Producer flushed successfully")
        except Exception as e:
            print(f"Error flushing producer: {e}")


    def __setup_db_(self, db_config): 
        ...