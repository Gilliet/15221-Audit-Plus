'''
Creates dictionaries courseNums and courseNames and populates them from 
courses.csv
'''

import csv
import ast

courseNums  = {}  # (keys = course numbers, values = course objects)          
courseNames = {}  # (keys = course names,   values = course objects)

class Course:
    def __init__(self, name, number, units, prereqs, coreqs, fall=True, 
                 spring=True):
        self.name = name
        self.number = number
        self.units = units
        self.prereqs = prereqs
        self.coreqs = coreqs
        self.fall = fall
        self.spring = spring

        courseNums[number] = self
        courseNames[name] = self

def createCourseDicts():
    '''Populates courseNums and courseNames from courses.csv'''
    
    reader = csv.reader(open('../data/courses.csv', 'rb'))

    reader.next() # skip the header line

    for row in reader:
        c = Course(row[0], int(row[1]), int(float(row[2])), 
                   ast.literal_eval(row[5]), ast.literal_eval(row[6]),
                   int(row[3]), int(row[4]))

createCourseDicts()
