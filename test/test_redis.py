import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

all_keys = redis_client.keys('*')

for key in all_keys:
    value = redis_client.get(key)
    if value is None:
        print(f"Key {key} does not exist")
    else:
        print(f"{key}: {value}")