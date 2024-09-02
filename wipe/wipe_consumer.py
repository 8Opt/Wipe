"""
A simple Fluvio consumer that consumes records from a topic.
"""

from datetime import datetime
from fluvio import Fluvio, Offset

class WIPEConsumer:
    """
    A class to consume records from a Fluvio topic.
    
    Attributes:
    ----------
    role : str
        The role of the consumer (in this case, 'customer').
    topic_name : str
        The name of the topic to consume from.
    partition : int
        The partition to consume from.
    consumer : Fluvio.partition_consumer
        The Fluvio consumer object.
        
    Methods:
    -------
    consume_records(num_records)
        Consumes a specified number of records from the topic.
    """

    ROLE = 'customer'

    def __init__(self, topic_name: str, partition: int):
        """
        Initializes the WIPEConsumer object.
        
        Parameters:
        ----------
        topic_name : str
            The name of the topic to consume from.
        partition : int
            The partition to consume from.
        """
        self.topic_name = topic_name
        self.partition = partition
        self.consumer = Fluvio.connect().partition_consumer(topic_name, partition)
        self.notification = []
        
    def consume_records(self, num_records: int) -> None:
        """
        Consumes a specified number of records from the topic.
        
        Parameters:
        ----------
        num_records : int
            The number of records to consume.
        """
        try:
            for idx, record in enumerate(self.consumer.stream(Offset.from_end(num_records))):
                print(f"Record {idx+1}: {record.value_string()}: timestamp: {datetime.now()}")
                self.notification.append(record.value_string())
                if idx >= num_records - 1:
                    break
        except Exception as e:
            print(f"Error consuming records: {e}")

    def flush(self): 
        """
        Delete notification
        """
        self.notification = []