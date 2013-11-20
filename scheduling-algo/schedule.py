from createCourseDictionary import *


""" degree requirements for CS -- in Conjunctive Normal Form """
CS = [[15128], [15122], [15150], [15210], [15213], [15251], [15451], [15221],   # CS CORE
      [15354, 15355, 15453, 15455, 21301, 21484],  # algorithms/complexity
      [2450, 5391, 5431, 10601, 11411, 15313, 15322, 15323, 15381, 15415, 15462, 16384, 16385],
      [15312, 15317, 15414, 15424, 21300, 80311], # logics/languages
      [15410, 15411, 15418, 15440, 15441], # distributed systems
      [21120], [21122], [21241],  # mathematics
      [21127, 15151],  # concepts
      [15359, 21325, 36217, 36225],  # probability
      [-15001], [-15002], [-15003], [-15004],  # science reqs
      [76101], [-15005], [-15006], [-15007],  # humanities categories
      [-15008], [-15009], [-15010]]        # humanit


""" prereqs are represnted in Disjunctive Normal Form -- a list of 
"""


# CS core
Course("Mathematical Foundations for Computer Science", 15151, 12, [], [], 0, 0)
Course("Fundamentals of Programming and Computer Science", 15112, 12, [], [], 1, 1)
Course("Great Theoretical Ideas", 15251, 12, [[15151, 15112], [21127,15112]], [],1, 1)
Course("Freshman Immigration Course", 15128, 1, [], [], 1, 0)
Course("Principles of Imperative Computation", 15122, 10, [[15112]], [[21127], [15151]], 1, 1)
Course("Principles of Functional Programming", 15150, 10, [[15151, 15112],[21127, 15112]], [], 1, 1)
Course("Parallel and Sequential Data Structures and Algorithms", 15210, 12, [[15150, 15122]], [],1,1)
Course("Introduction to Computer Systems", 15213, 12, [[15122]], [], 1, 1)
Course("Great Theoretical Ideas in Computer Science", 15251, 12, [[15112, 15151], [15112, 21127]], [],1,1)
Course("Algorithm Design and Analysis", 15451, 12, [[15251, 15210, 21241]], [], 1,1)
Course("Technical Communication for Computer Scientists", 15221, 9, [[76101]], [], 1,1)
# Algorithms/Complexity
Course("Computational Discrete Mathematics", 15354, 12, [[15251]], [], 1,0)
Course("Modern Computer Algebra", 15355, 9, [[15251]], [], 1,0)
Course("Formal Languages, Automata, and Computability", 15453, 9, [[21228], [15251]], [],0,1)
Course("Undergraduate Complexity Theory", 15455, 9, [[15251]], [], 1,0)
Course("Combinatorics", 21301, 9, [[21122,21228],[21122,15251]], [], 1,0)
Course("Graph Theory", 21484, 9, [[21228,21241],[21228,21242],[15251,21241],[15251,21241]], [],0,1)
# Applications
Course("Automation of Biological Research", 2450, 9, [[15122]], [], 1,0)
Course("Designing Human Centered Software", 5391, 12, [], [], 0, 1)
Course("Software Structures for User Interfaces", 5431, 6, [], [[05433]], 1,0)
Course("Machine Learning", 10601, 12, [[15122,21127],[15122,15151]], [[21325],[15359],[36225],[36217]], 1,1)
Course("Natural Language Processing", 11411, 12, [[15122]], [], 0,1)
Course("Foundations of Software Engineering", 15313, 12, [[15214]], [],1,0)
Course("Introduction to Computer Music", 15322, 9, [[15112]], [], 0,1)
Course("Computer Music Systems and Information Processing", 15323, 9, [[15122]], [], 1,0)
Course("Artificial Intelligence: Representation and Problem Solving", 15381, 9, [[15122, 15211]], [],1,0)
Course("Database Applications", 15415, 12, [[15210],[15211, 15213]], [], 0,1)
Course("Computer Graphics", 15462, 12, [[21259, 15213, 21241],[15213,18202]], [], 1,1)
Course("Robot Kinematics and Dynamics", 16384, 12, [[15122],[18202],[24311],[21241],[16311]],[],1,0)
Course("Computer Vision", 16385, 9, [[18202,15122],[15122,21259,21241]], [], 0,1) 
# Logics/Languages
Course("Foundations of Programming Languages", 15312, 12, [[15210,15251],[15212]], [],0,1)
Course("Constructive Logic", 15317, 9, [[15210],[15212]], [], 1,0)
Course("Bug Catching: Automated Program Verification and Testing", 15414, 9, [[15122, 15251],[15211,15251]],[],1,0)
Course("Special Topic: Foundations of Cyber-Physical Systems", 15424, 12, [[15122, 15251, 21122]], [], 0,0)
Course("Basic Logic", 21-300, 9, [[15251],[21228],[21373]], [],1,0 )
Course("Undecidability and Incompleteness", 80311, 9, [[80210],[80211],[21300],[80310],[15251]], [],0,1)
# Software Systems
Course("Operating System Design and Implementation", 15410, 12, [[15213]], [], 1,1)
Course("Compiler Design", 15411, 12, [[15213],[15312]], [],1,0 )
Course("Parallel Computer Architecture and Programming", 15418, 12, [[15213]], [],0,1)
Course("Distributed Systems", 15440, 12, [[15213]], [], 0,1)
Course("Computer Networks", 15441, 12, [[15213]], [],1,1)
# Mathematics
Course("Differential and Integral Calculus", 21120, 10, [], [],1,1)
Course("Integration, Differential Equations and Approximation", 21122, 10, [[21112],[21120]], [], 1,1)
Course("Concepts of Mathematics", 21127, 10, [], [],1,1)
Course("Matrices and Linear Transformations", 21241, 10, [], [],1,1)
Course("Matrix Theory", 21242, 10, [], [],1,1)
# Probability
Course("Probability and Computing", 15359, 12, [[15251, 21259, 21241]], [],0,1)
Course("Probability", 21325, 9, [[21259],[21268],[21269]], [],1,0)
Course("Probabliity Theory and Random Processes", 36217, 9, [[21122],[21112],[21259],[21256],[21123]],[],1,1)
Course("Introduction to Probability Theory", 36225, 9, [[21256],[21259]], [],1,0)

# Science
Course("Laboratory Science Requirement", -15001, 9, [], [],1,1)
Course("Engineering or Science 1", -15002, 9, [], [],1,1)
Course("Engineering or Science 2", -15003, 9, [], [],1,1)
Course("Engineering or Science 3", -15004, 9, [], [],1,1)


# Humanities
Course("Interpretation and Argument", 76101, 9, [], [],1,1)
Course("Category 1 Humanity", -15005, 9, [], [],1,1)
Course("Category 2 Humanity", -15006, 9, [], [],1,1)
Course("Category 3 Humanity", -15007, 9, [], [],1,1)

Course("Humanity Elective 1", -15008, 9, [], [],1,1)
Course("Humanity Elective 2", -15009, 9, [], [],1,1)
Course("Humanity Elective 3", -15010, 9, [], [],1,1)



global nodata
nodata = Course("NODATA", -1, -1, [[-1]], [-1],1,1) # we won't suggest courses we don't have data for





