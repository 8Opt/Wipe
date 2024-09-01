import time

from controller.pubsub import pub_produce_articles


while True: 
    pub_produce_articles()  # Avg of 35 secs per call.
    time.sleep(10)
