#!/usr/bin/python
# API reference : https://github.com/andymccurdy/redis-py
import redis


redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = None;
pubsubptr = None;

def sample_redis():
    """ Sample code to access redis server """
    
    try:
    
        # The decode_repsonses flag used to give response as python strings (default encoding utf-8)
        global r;
        global pubsubptr;  

        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
   
        # handler to hold pubsub method
        pubsubptr = r.pubsub();         
        # pubsubptr = r.pubsub(ignore_subscribe_messages=True);         
 
        r.set("user1", "apple")

        # step 5: Retrieve the hello message from Redis
        msg = r.get("user1")
        print msg        
 
 
    except Exception as e:
        print e



def multi_exec():
    """ MULTI and EXEC in Redis can be tried using pipeline command """
    pipe = r.pipeline();
    pipe.set("user2","mango");
    pipe.get("user1");
    pipe.execute()

def my_cb(message):
    """  callback to retrieve the message from channel """
    print "+++++++++++++++++++++++++++++++++++++++++++++++++"
    print "        " + message['data'];
    print "+++++++++++++++++++++++++++++++++++++++++++++++++"


def subscribe_cbmethod():
    """ subscribe using callback method 
        channel name is my-channel
        callback name is my_cb """

    pubsubptr.subscribe(**{'my-channel': my_cb}); 
    print pubsubptr.get_message(); # each time get_message is used to get subscribe message
    # to ignore this use
    # r.pubsub(ignore_subscribe_messages=True)
    r.publish('my-channel', 'Global Warming - world has to rise to stop')
    pubsubptr.get_message();

if __name__ == '__main__':
    sample_redis()
    multi_exec();
    subscribe_cbmethod();
    #pubsubptr.subscribe('ch1');
    #print pubsubptr.get_message();
    #r.publish('ch1','some data');
    #print pubsubptr.get_message();
