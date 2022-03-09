#!/usr/bin/python
from redis import StrictRedis

hostname='3.233.79.93'
password='telematica'
channel='1'

r = StrictRedis(host=hostname,port=6379,password=password,db=0)
publisher = r.pubsub()

while True:
    message=input("Describe play, or press [Enter] to quit: ")

    if not message:
        break
    else:
        r.publish(channel,message)
        #print message

print ("Publish program ended.")