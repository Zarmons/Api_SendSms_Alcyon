from redis.exceptions import ResponseError
from redis import Redis

redis_client = Redis(
  host= 'us1-wise-chimp-38457.upstash.io',
  port= '38457',
  password= 'ac3a9c11015a4e7f99f6592b6496ccd0'
)

def save_hash(key: str, data: dict):
    try:
        redis_client.hset(name=key, mapping=data)
    except ResponseError as e:
        print(e)


def get_hash(key: str):
    try:
        return redis_client.hgetall(name=key)
    except ResponseError as e:
        print(e)

def delete_hash(key: str, keys: list):
    try:
        redis_client.hdel(key, *keys)
    except ResponseError as e:
        print(e)
    