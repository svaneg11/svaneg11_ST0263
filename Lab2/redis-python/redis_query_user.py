#!/usr/bin/python
from redis import StrictRedis
from datetime import datetime
import random

hostname='3.233.79.93'
password='telematica'
userid='user' + str(random.randint(0, 999))
age = str(random.randint(0, 99))


r = StrictRedis(host=hostname,port=6379,password=password,db=0)

def addNewLogin(user,age):
    print("Logging entry for " + user + " with age " + age)
    time = str(datetime.now())
    r.lpush('svaneg11:logins',user + " " + age + " " + time)
    r.ltrim('svaneg11:logins',0,2)
    
def getList():
    list = r.lrange('svaneg11:logins',0,-1)
    print(list)

addNewLogin(userid,age)
getList()