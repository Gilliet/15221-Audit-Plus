# generate csv of schedules
# $ python gen_sample_schedules.py <iters>


from problem import *
import sys

if len(sys.argv) < 2:
    print "Prints out <iter> schedules as comma seperated values"
    print "   usage:  python gen_sample_schedues.py <iters>"
    exit(1)

sems = dict()
sems[0] = [15112, 15128]
init = (CS, sems, "fall")

a = scheduleProblem(init)
print "init:", init
print "a.initial:", a.initial

schedules = []
for i in range(int(sys.argv[1])):
    x = depth_first_tree_search(a).state[1]
    x.pop(0, None)

    for courseList in x.values():
        for course in courseList:
            temp = str(course) + ", "
            sys.stdout.write(temp)
    sys.stdout.write("\n")
    schedules.append(x)

print "\n\n\n\n"

for i in range(len(schedules)):
    print ""
    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
    print "SCHEDULE: ", i+1
    for j in range(len(schedules[i])):
        courseList = schedules[i][j+1]
        print "Semester: ", j+1
        for course in courseList:
            print course, ": " + courseNums[course].name
    print "\n"
   
