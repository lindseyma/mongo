from pymongo import MongoClient
import csv

f = open("peeps.csv") #add people
d = csv.DictReader(f)

mainDict = {}

server = MongoClient('127.0.0.1')
db = server.mongo
server.drop_database('mongo')#clears database

c = db.students

for student in d: # Writes in the students
    mainDict[student['id']] = student

f.close()

f = open("courses.csv") #add grades
d = csv.DictReader(f)

for course in d:
    for student in mainDict:
        if mainDict[student]['id'] == course['id']:
            mainDict[student][course['code']] = course['mark']

for i in mainDict:
    c.insert_one(mainDict[i]);

