from pymongo import MongoClient

server = MongoClient('127.0.0.1')
db=server.jl.students
cursor = db.find()
ret=[]

for student in cursor:
    total=0
    a=0
    for course in student.courses:
        total+=course.mark
        a+=1
    avg=total/a
    print "name: " + student.name
    print "id: " + student.id
    print "avg: " + str(avg)
