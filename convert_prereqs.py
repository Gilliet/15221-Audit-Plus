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
with open('prereqs.csv', 'rb') as f:
    reader = csv.reader(f)
    numRows = 0
    specialRows = ['18712'] # rows with special prereqs that couldn't be parsed
    specialRowMessages = []
    for row in reader:
        if (row[0] in specialRows):
            specialRowMessages.append("Could not parse {0}:{1}".format(
                    row[0], row[1]))
        else:
            print "{0}, {1}".format(row[0], parsePrereqString(row[1]))
        numRows += 1
    
    for message in specialRowMessages: print message
    print "Total classes:", numRows
