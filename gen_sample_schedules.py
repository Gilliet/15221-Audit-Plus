# generate csv of schedules
# $ python gen_sample_schedules.py <iters>


from problem import *
import sys

if len(sys.argv) < 2:
    print "Prints out <iter> schedules as comma seperated values"
    print "   usage:  python gen_sample_schedues.py <iters>"
    exit(1)

a = scheduleProblem(initialState)

for i in range(int(sys.argv[1])):
    x = depth_first_tree_search(a).state[1]

    for courseList in x.values():
        for course in courseList:
            temp = str(course) + ", "
            sys.stdout.write(temp)
    sys.stdout.write("\n")

print "\n\n\n\n"
for i in range(int(sys.argv[1])):
    x = depth_first_tree_search(a).state[1]

    for courseList in x.values():
        for course in courseList:
            temp = str(course) + ": " + courseNums[course].name + ", "
            sys.stdout.write(temp)
    sys.stdout.write("\n")

        

        
