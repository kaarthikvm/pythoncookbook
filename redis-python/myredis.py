#!/usr/bin/python
import redis


redis_host = "localhost"
redis_port = 6379
redis_password = ""


def sample_redis():
    """ Sample code to access redis server """
    
    try:
    
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
        r.set("user1", "granted access")

        # step 5: Retrieve the hello message from Redis
        msg = r.get("user1")
        print msg        
    
    except Exception as e:
        print e


if __name__ == '__main__':
    sample_redis()
