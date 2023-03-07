import pymongo
import threading
from  pymongo import MongoClient
cl=MongoClient("mongodb+srv://josetellis2018:dHmjZHB5MZgPsH0f@cluster0.ghrj9wz.mongodb.net/?retryWrites=true&w=majority")
db=cl['hcl_data']
col=db['users']
lock=threading.Lock
def read():

    result=col.find({},{"_id":0})
    for r in result:
        print(r)

read()