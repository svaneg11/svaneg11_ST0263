#!/usr/bin/python
from redis import StrictRedis

hostname='3.233.79.93'
password='telematica'

r = StrictRedis(host=hostname,port=6379,password=password,db=0)

def getPacktWelcome():
    #GET value stored in packt:welcome
    print("Displaying current welcome message...")
    value = r.get('svaneg11:welcome')
    print("message = " + str(value))

def setPacktWelcome():
    #SET new value packt:welcome
    print("Writing \"Hello world from Python!\" to Redis...")
    r.set('svaneg11:welcome','Hello world from Python!')

getPacktWelcome()
setPacktWelcome()
getPacktWelcome()
