from pymongo import MongoClient
import csv

server = MongoClient('127.0.0.1')
db=server.jl.students
cursor = db.find()
ret=[]

for student in cursor:
    total=0
    a=0
    for mark in student['marks']:
        total+=mark['mark']
        a+=1
    avg=total/a
    print "name: " + student['name']
    print "id: " + str(student['id'])
    print "avg: " + str(avg)
