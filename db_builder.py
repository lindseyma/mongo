from pymongo import MongoClient
import csv

f = open("peeps.csv")
d = csv.DictReader(f)

server = MongoClient('127.0.0.1')

db = server.mongo

c = db.students

for thing in d: # Writes in the students
    c.insert_one(thing)

print c.count()
print c.find_one({'name': 'kruder'})

f.close()

f = open("courses.csv")
d = csv.DictReader(f)

######## I'm not sure if we're supposed to put the information in the same documents
#or different ones
