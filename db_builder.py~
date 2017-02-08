from pymongo import MongoClient
import csv

f = open("peeps.csv") #add people
d = csv.DictReader(f)

mainDict = {}

server = MongoClient('127.0.0.1')
db = server.jl
server.drop_database('jl')#clears database

s = db.students

for student in d: # Writes in the students
    student['id'] = int(student['id'])
    student['age'] = int(student['age'])
    mainDict[student['id']] = student

f.close()


for student in mainDict:
    marks = []
    sid = mainDict[student]['id']
    f = open("courses.csv") #add grades
    d = csv.DictReader(f)

    for course in d:
        course['id'] = int(course['id'])
        if course['id'] == sid:
            course['mark'] = int(course['mark'])
            marks.append(course)
    mainDict[student]['marks'] = marks

f.close()
    
for i in mainDict:
    s.insert_one(mainDict[i]);

f = open("teachers.csv")
d = csv.DictReader(f)

t = db.teachers

for teacher in d:
    teacher['period'] = int(teacher['period'])
    peeps = []
    for peep in s.find({'marks.code' : teacher['code']}):
        peeps.append(peep['id']);
    teacher['peeps'] = peeps
    t.insert_one(teacher)

f.close()
    
