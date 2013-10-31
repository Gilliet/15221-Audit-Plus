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
        schedule: dictionary of semeseters and classes

    Returns:
        true/false
    """
    classes = sum(schedule.values(), [])
    for x in courseNums[courseNum].prereqs:
        if x not in classes:
            return false
    return true

def possibleClasses(courses, degree_reqs):
    """ Returns a list of course numbers that satisfy degree requirements 
        and have all prerequisites met. 

    Args:
        couses: a list of courses (by number) taken to date
        degree_reqs: a list of degree requirements, in CNF

    Returns:
        A list of courses that could be taken in the next semester
    """
    course_set = set(courses)
    possible_classes = []
    for disjunction in degree_reqs:  # reqs in CNF
        for course in disjunction:
            prereqs = (courseNums.get(course, nodata)).prereqs # prereqs in DNF
            if not prereqs: possible_classes.append(course)
            for conjunction  in prereqs:
                if set(conjunction).issubset(course_set):
                    possible_classes.append(course)

    return possible_classes   # very simple. TODO: coreqs, antireqs, etc. 

                





degree_reqs = CS  # conjunctive normal form
classes = []      # disjunctive normal form

""" state is 2-tuple:
    0) remaining degree requirements
    1) (key=int, value=int list) dictionary of semesters and classes 
       where dict[0] = existing course credit
"""
class scheduleProblem(Problem):
    # actions are a list of classes to take in a semester
    def actions(self, state):  # NOT CORRECT
        (reqs, sems) = state
        courses = sum(sems.values(), [])
        possible_courses = possibleClasses(courses, reqs)

        temp = set([frozenset((x,y)) for x in possible_courses for y in possible_courses if x !=y])
        schedules = []
        for a in temp:
            schedules.append(list(a))
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
sems[0] = [15112]
initialState = (CS, sems)
a = scheduleProblem(initialState)
print a.actions(initialState)

