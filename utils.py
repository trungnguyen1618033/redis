import redis
import json
from datetime import timedelta

redis_host = 'localhost'
redis_port = '6379'


def redis_json():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
    except Exception as e:
        print(e)
    return r

rds = redis_json()

class test:
    def set(cache_key, data):
        data = json.dumps(data)
        rds.setex(cache_key, timedelta(minutes=1), data)

        return True

    def get(cache_key):
        cache_data = rds.get(cache_key)
        print(cache_data)
        if not cache_data:
            return None

        cache_data = json.loads(rds.get(cache_key))
        return cache_data