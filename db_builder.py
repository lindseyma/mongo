from pymongo import MongoClient
import csv

f = open("peeps.csv") #add people
d = csv.DictReader(f)

mainDict = {}

server = MongoClient('127.0.0.1')
db = server.jl
server.drop_database('jl')#clears database

c = db.students

for student in d: # Writes in the students
    sDict = {}
    sDict['id'] = int(student['id'])
    sDict['name'] = student['name']
    sDict['age'] = int(student['age'])
    mainDict[sDict['id']] = sDict

f.close()


for student in mainDict:
    marks = []
    sid = mainDict[student]['id']
    f = open("courses.csv") #add grades
    d = csv.DictReader(f)

    for course in d:
        if int(course['id']) == sid:
            cDict = {}
            cDict['code'] = course['code']
            cDict['mark'] = int(course['mark'])
            marks.append(cDict)
    mainDict[student]['marks'] = marks

print mainDict
    
for i in mainDict:
    c.insert_one(mainDict[i]);


    
