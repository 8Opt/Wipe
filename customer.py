import time
import random
from controller.pubsub import sub_catch_articles, sub_read_articles

while True: 
    sub_catch_articles()
    time.sleep(10)
    
    rand_idx = random.randint(a=0, b=10)
    if rand_idx % 2 == 0: 
        sub_read_articles()