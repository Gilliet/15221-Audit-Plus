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
    for r in reqs:
        for c in classes:
            if not c in r: new_reqs.append(r)
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





degree_reqs = CS  # conjunctive normal form
classes = []      # disjunctive normal form

""" state is 2-tuple:
    0) remaining degree requirements
    1) (key=int, value=int list) dictionary of semesters and classes 
       where dict[0] = existing course credit
"""
class scheduleProblem(Problem):
    # actions are a list of classes to take in a semester
    def actions(self, state):
        pass
        # get list X of possible semesters
        # and return set of states, where each state = x :: state, forall x <- X

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
sems[0] = []
initialState = (CS, sems)
a = scheduleProblem(initialState)

