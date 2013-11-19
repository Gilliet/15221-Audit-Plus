# Using information from neatenedSemesterData.csv, prereqs.csv, and coreqs.csv,
# creates a file courses.csv that is like neatenedSemesterData.csv only with 
# prereqs and coreqs added as fields. See makeCoursesCSV function for the
# order.

import csv
from sympy import sympify
from sympy.logic.boolalg import to_dnf
from sympy.core.sympify import SympifyError

# Takes a prereq string ps and returns a string version of a DNF as outputted 
# by sympy, or the empty string if it could not be parsed by sympy
# Assumes ps is not the empty string
def stringToDNF(ps):
    
    # Replace ands and ors so that sympify parses correctly
    ps = ps.replace("and", "&")
    ps = ps.replace("or", "|")

    # Need to remove dashes and add a letter before each course number
    while "-" in ps:
        i = ps.find("-")
        ps = ps[:(i-2)] + "c" + ps[(i-2):i] + ps[(i+1):]

    try:
        psSympified = sympify(ps)
    except SympifyError:
        return ""

    return str(to_dnf(psSympified))

# Takes in string of prereqs from scraper and returns those prereqs in a list
# in DNF form
def parsePrereqString(prereqString):
    if (prereqString == ""): return []

    # string version of DNF given by sympy
    prereqDNF = stringToDNF(prereqString)
    if prereqDNF == "":
        print "Could not parse", prereqString
        return

    # Remove the "Or" and "And"s and spaces
    prereqDNF = prereqDNF.replace("Or", "")
    prereqDNF = prereqDNF.replace("And", "")
    prereqDNF = prereqDNF.replace(" ", "")

    # Remove surrounding parentheses
    prereqDNF = prereqDNF[1:(len(prereqDNF)-1)]

    # Get each clause of the DNF
    # First get clauses in parentheses
    clauseList = []
    while "(" in prereqDNF:
        p1 = prereqDNF.find("(")
        p2 = prereqDNF.find(")")
        # The clause is everything between the open and close parentheses
        clause = prereqDNF[(p1+1):p2]
        clauseList.append(clause)
        # If the clause is not the last clause in the list, remove comma after
        # the clause from the prereq string
        if (p2 < len(prereqDNF) - 1): 
            prereqDNF = prereqDNF[:(p2+1)] + prereqDNF[(p2+2):]
        # Remove clause from the list
        prereqDNF = prereqDNF[:p1] + prereqDNF[(p2+1):]
    
    # Then get the rest of the clauses, if there are any
    if (prereqDNF != ""):
        clauseList += prereqDNF.split(",")

    prereqList = []

    # Parse the clauses into a list of lists of course numbers
    # If a course number doesn't parse, make it -2 (special flag)
    for clause in clauseList:
        courseList = []
        courses = clause.split(",")
        for course in courses:
            try:
                courseNum = int(course[1:]) # remove the first letter
            except ValueError:
                # The prereq was a special, text prereq
                # Print a message that lets us know about it
                # Also mark the course number as -2 (a special prereq flag)
                print "Could not parse", course, "as a course number"
                print "clauseList = ", clauseList
                courseNum = -2
            courseList.append(courseNum)
        prereqList.append(courseList)

    return prereqList

# Open csv and for each row, print out the course number and a list of its 
# prereqs in DNF format
# courses - dictionary of course dictionaries that are partially filled in
# reqString - either "prereqs", "coreqs", or "antireqs"
# specialCourses - list of strings denoting courses that have 
#                requirements that are not course numbers (ex. have to be a 
#                senior to take a class)
def fillInReqs(courses, reqString, specialCourses):
    csvFile = reqString + ".csv"
    reader = csv.reader(open(csvFile, 'rb'))
    unmatchedCourses = [] # any courses that were in the req file but not in
                          # neatenedSemesterData.csv

    for row in reader:
        if (row[0] not in specialCourses):
            if (row[0] in courses.keys()):
                courses[row[0]][reqString] = parsePrereqString(row[1])
            else:
                unmatchedCourses.append(row)

    print "Added", reqString
    return (courses, unmatchedCourses)


def fillInPrereqs(courses):
    # Add special prereqs
    courses['18712']['prereqs'] = [[18300, 18310, 18402], 
                                   [18300, 18310, 33439]]
    courses['54108']['prereqs'] = [[54107]]

    return fillInReqs(courses, "prereqs", ['18712', '54108'])

def fillInCoreqs(courses):
    return fillInReqs(courses, "coreqs", [])

def fillInAntireqs(courses):
    # Antireq courses are formatted without dashes, so our program won't be
    # able to parse them the same
    # Since there's only 3, though, it's easy enough to enumerate them here
    if (('18342' not in courses.keys()) or ('18348' not in courses.keys()) or
        ('18349' not in courses.keys())):
        unmatchedCourses = ['18342', '18348', '18349']
    else:
        unmatchedCourses = []
        courses['18342']['antireqs'] = [[18348],[18349]]
        courses['18348']['antireqs'] = [[18342],[18349]]
        courses['18349']['antireqs'] = [[18342],[18348]]

    print "Added antireqs"
    return (courses, unmatchedCourses)


# Makes a dictionary courses containing a dictionary containing course 
# dictionaries, where each course dictionary has keys name, num, units, fall,
# spring, prereqs, coreqs, and antireqs. Helper function for makeCoursesCSV.
#
# Returns the completed courses dictionary.
def makeCoursesDict():
    sem_data = csv.DictReader(open("neatenedSemesterData.csv", 'rb'),
                              ["name", "num", "units", "fall", "spring"])
    
    num_courses = 0
    courses = dict() # dictionary of courses, where each course is a dictionary
                     # containing the name, course number, # units, offered in
                     # fall or spring, prereqs, coreqs, and antireqs

    # First populate courses dictionary with course info (not including reqs.)
    for row in sem_data:
        courses[row['num']] = row
        num_courses += 1

    # Then fill in all the requirements
    (courses, unmatchedPrereqs) = fillInPrereqs(courses)
    (courses, unmatchedCoreqs) = fillInCoreqs(courses)
    #(courses, unmatchedAntireqs) = fillInAntireqs(courses)
    
    # Print out if there are any unmatched classes
    if (unmatchedPrereqs): print "Unmatched prereqs:", unmatchedPrereqs
    if (unmatchedCoreqs): print "Unmatched coreqs:", unmatchedCoreqs
    #if (unmatchedAntireqs): print "Unmatched antireqs:", unmatchedAntireqs

    return courses
    

# Given a dictionary courses containing dictionaries with course information,
# encodes that into a csv called courses.csv

# Each row documents a course, with the fields as:
# name, number, units, fall, spring, prereqs, coreqs
def makeCoursesCSV():
    courses = makeCoursesDict()

    writer = csv.DictWriter(open('courses.csv', 'wb'), 
                            ["name", "num", "units", "fall", "spring", 
                             "prereqs", "coreqs"])
    writer.writeheader()

    for course in courses.keys():
        writer.writerow(courses[course])

makeCoursesCSV()
