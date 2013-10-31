import search

""" state is 3-tuple:
    1) courses taken to-date
    2) remaining degree requirements
    3) (key=int, value=int list) dictionary of semesters and classes 
"""

class scheduleProblem(Problem):
    def actions(self, state):
        # get list X of possible semesters
        # and return set of states, where each state = x :: state, forall x <- X


    # return True if the state is a goal
    # state is goal if all requirements for degree are met
    def goal_test(self, state):
