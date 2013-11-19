""" get course catalog information without using scrapy """
import urllib2
import re

def getCourseCodefromNum(num):
    num = str(num)
    if len(num) == 4:
        num = "0" + num
    return num[0:2] + "-" + num[2:]

def getCourseInfo(courseNum):
    """ inputs a courseID string (eg, '15-251')
        opens coursecatalog web page and uses regex to get relevant course data
        returns: course information (as object?)
    """

    courseCode = getCourseCodefromNum(courseNum)

    url = 'http://coursecatalog.web.cmu.edu/ribbit/?page=getcourse.rjs&code=' + courseCode
    response = urllib2.urlopen(url)
    html = response.read()

    prereq_regex = re.compile('Prerequisite(?:s)?:(.*?)(?:\.|C|<)')
    prereq_match = prereq_regex.search(html)
    if prereq_match != None:
        print "Prereqs:", prereq_match.group(1)

    coreq_regex = re.compile('Corequisite(?:s)?:(.*?)(?:\.|C|<)')
    coreq_match = coreq_regex.search(html)
    if coreq_match != None:
        print "Coreqs:", coreq_match.group(1)

    antireq_regex = re.compile('Anti-requisite(?:s)?:(.*?)(?:\.|C|<)')
    antireq_match = antireq_regex.search(html)
    if antireq_match != None:
        print "Antireqs:", antireq_match.group(1)


    
