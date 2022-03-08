#!/usr/bin/python
from redis import StrictRedis

hostname='3.233.79.93'
password='telematica'
channel='1'

r = StrictRedis(host=hostname,port=6379,password=password,db=0)
channels = r.pubsub()
channels.subscribe(channel)

for message in channels.listen():
    if message['data']=='END':
        break

    if message['data']!=1:
        print(message['data'])

channels.unsubscribe(channel)
print("Unsubscribed")