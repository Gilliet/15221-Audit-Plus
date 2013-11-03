tech-comm-project
=================

A place for us to keep all our junk for tech comm! 

A really basic scheduling program! Right now, this uses includes only Computer
Science classes that meet degree requirements. The CS degree requirements are 
hard-coded in `schedule.py`. We are working on automagically getting more
scheduling data. Generated schedules have 2 classes per semester, and meet
prerequisite requirements (but not corequisites!). 

## Usage
To get a feel for the way schedules are generated, open up `problem.py`:
Note that `a` is the temporary name of the scheduling problem instance.

    $ python -i problem.py
    >>> depth_first_tree_search(a)

Depth-first search is reasonably fast, but does not return optimal schedules.
Breadth-first search is unreasonably slow. Way too slow.


## Files


*    schedule.py -- computer science scheduling information

*    problem.py  -- a first attempt at a problem definition for schedule building
                 this contains the relevant logic

*    gen_sample_schedules.py -- prints out schedules as csv

*    aima/*      -- code from Artificial Intellgience: A Modern Approach
                 (for search algorithms)
                 

