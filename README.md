Audit+: an automagical schedule 
=================

This is a scheduling program built for 15-221 at Carnegie Mellon University.

A really basic scheduling program! Right now, this uses includes only Computer
Science classes that meet degree requirements. The CS degree requirements are
hard-coded in `scheduling-algo/schedule.py`. We are working on automagically
getting more scheduling data. Current efforts on this front are in `scraping/`
Generated schedules have 2 classes per semester, and meet prerequisite
requirements (but not corequisites!). 

## Usage
To get a feel for the way schedules are generated, open up `scheduling-algo/problem.py`:
Note that `a` is the temporary name of the scheduling problem instance.

    $ cd scheduling-algo
    $ python -i problem.py
    >>> depth_first_tree_search(a)

Depth-first search is reasonably fast, but does not return optimal schedules.
Breadth-first search is unreasonably slow. Way too slow.

To get prerequisite information for courses, open up `scraping\read_catalog.py`:

    $ cd scraping
    $ python -i read_catalog.py
    >>> getCourseInfo(15122)
    Prereqs:  15-122
    Coreqs:  21-127

Course numbers should not have leading zeros. This functions downloads prerequisite 
information from Carnegie Mellon's undergraduate course catalog.


## Files


*    scheduling-algo/
    *       schedule.py -- computer science scheduling information

    *       problem.py  -- a first attempt at a problem definition for schedule building
                           this contains the relevant logic

    *       gen_sample_schedules.py -- prints out schedules as csv

    *       aima/*      -- code from Artificial Intellgience: A Modern Approach
                           (for search algorithms)

*    scraping/
    *       read_catalog.py -- script to download prereq info from CMU course catalog
    *       scrapy/         -- work in progress on scrapy implementation

                 

