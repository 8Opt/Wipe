"""
A simple Fluvio producer that produces records to a topic.
"""
import subprocess

from fluvio import Fluvio

class WipeProducer:
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

    def __init__(self, topic_name: str, partition: int):
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
        
    def produce_records(self, event: str) -> None:
        """
        Produces a specified event.
        
        Parameters:
        ----------
        event : str
            The information of the event
        """
        try:
                self.producer.send_string(event)
                
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

    def __create_topic(self, topic_name:str):
        """
        Create a topic. 

        Parameters: 
        ----------
        topic_name: str
            The name of the topic
        """
        try:
            shell_cmd = ['fluvio', 'topic', 'create', topic_name]
            subprocess.run(shell_cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Command {e.cmd} failed with error {e.returncode}')