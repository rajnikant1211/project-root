import redis
import json
from datetime import datetime

r = redis.Redis(host='localhost', port=6379, db=0)

def save_memory(key, data):
    data['timestamp'] = str(datetime.now())
    r.set(key, json.dumps(data))

def get_memory(key):
    value = r.get(key)
    return json.loads(value) if value else None