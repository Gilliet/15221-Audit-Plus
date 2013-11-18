import itertools
import random
import sys

from aima.search import *
from schedule import *


def removeReqs(classes, reqs):
    """ Removes requirements that are satisifed by classes

    Args:
        classes: an int list of course numbers
        reqs: a list of degree requirements, in CNF 

    Returns:
        A list of remaining requirements, in CNF
    """
    new_reqs = []
    for disjunction in reqs:
        satisfied = False
        for c in disjunction:
            if c in classes:
                satisfied = True
        if not satisfied:
            new_reqs.append(disjunction)
        
    return new_reqs

def prereqsSatisfied(courseNum, schedule):
    """ Return true if the prereqs for course are satisfied in current state
        and no antirequisites 

    Args:
        courseNum: number of course to check (int)
        schedule: dictionary of semesters and classes

    Returns:
        true/false
    """
    classes = sum(schedule.values(), [])
    prereqs = courseNums.get(courseNum, nodata).prereqs
    if not prereqs: return True
    for conjunction in prereqs:
        satisfied = True
        for course in conjunction:
            if course not in classes:
                satisfied = False
        if satisfied: return True
    return False

def coreqsSatisfied(semester, courses_taken):
    """ Return true if the coreqs for each course in the semester are satisfied.
        Coreqs are satisfied if each coreq is also in the schedule, or if the 
        coreq has previously been taken.

    Args:
        semester: a list of classes to take in a semester (int list)
        courses_taken: a list of classes previously taken (int list)

    Returns:
        true/false
    """

    for courseNum in semester:
        coreqs = courseNums.get(courseNum, nodata).coreqs# in disjunctive normal form
        if not coreqs: continue


        satisfied = False
        for conjunction in coreqs:
            for course in conjunction:
                if (course in semester) or (course in courses_taken):
                    satisfied = True
        if not satisfied: return False
    return True


def possibleClasses(schedule, degree_reqs):
    """ Returns a list of course numbers that satisfy degree requirements 
        and have all prerequisites met. 

    Args:
        schedule: a dictionary of semesters and classes
        degree_reqs: a list of degree requirements, in CNF

    Returns:
        A list of courses that could be taken in the next semester
    """
    courses = sum(schedule.values(), [])
    course_set = set(courses)
    possible_classes = []
    for disjunction in degree_reqs:  # reqs in CNF
        random.shuffle(disjunction)
        for course in disjunction:
            if prereqsSatisfied(course, schedule):
                possible_classes.append(course)
                break



    random.shuffle(possible_classes)
    return possible_classes   # very simple. TODO: coreqs, antireqs, etc. 

                

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s,r) for r in range(len(s) +1))


degree_reqs = CS  # conjunctive normal form
classes = []      # disjunctive normal form

""" state is 2-tuple:
    0) remaining degree requirements
    1) (key=int, value=int list) dictionary of semesters and classes 
       where dict[0] = existing course credit
"""
class scheduleProblem(Problem):
    def __init__(self, initialState):
        (reqs, sems) = initialState
        classes = sum(sems.values(), [])
        new_reqs = removeReqs(classes, reqs)
        self.initial = (new_reqs, sems)


    # actions are a list of classes to take in a semester
    def actions(self, state):  # NOT CORRECT
        (reqs, sems) = state
        print state, "\n"
        courses = sum(sems.values(), [])
        possible_courses = possibleClasses(sems, reqs)

        temp = powerset(possible_courses)
        schedules = []
        for x in temp:
            schedules.append(list(x))
        
        # impose maximum length on schedules
        schedules = filter(lambda x: len(x) <= 3, schedules) 

        # schedules must have prereqs satisfied
        classes_taken = sum(state[1].values(), [])
        schedules = filter(lambda x: coreqsSatisfied(x, classes_taken), schedules)
        return schedules


    def result(self, state, course_list):
        (reqs, sems) = state
        new_reqs = removeReqs(course_list, reqs)
        next_sem = max(sems.keys()) +1
        new_sems = sems.copy()

        new_sems[next_sem] = course_list
        return(new_reqs, new_sems)


    # return True if the state is a goal
    # state is goal if all requirements for degree are met
    def goal_test(self, state):
        (reqs, sems) = state
        return not reqs


sems = dict()
sems[0] = [15112, 15151, 21241, 76101, 15122, 15128]
init = (CS, sems)
a = scheduleProblem(init)
global initialState
initialState = a.initial


