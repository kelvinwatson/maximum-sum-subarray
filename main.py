#!/usr/bin/env python
#title          :main.py
#description    :Main file to parse input from MSS_TestProblems.txt and call
#                max sum subarray implementations
#author         :project group 2: Joseph Barlan, Jeff Mueller, Kelvin Watson
#creation date  :13 October 2015
#last modified  :13 October 2015
#usage          :python main.py
#notes          :
#python_version :2.6.6
#==============================================================================
import maxSumSubarray


arrays = []
with open("MSS_TestProblems.txt", "r") as f:
    for line in f:
        line = line.replace("[", "")
        line = line.replace("]", "")
        line = line.replace("\n", "")
        mss = line.split(",")
        mss = [int(i) for i in mss]
        print mss
        arrays.append(mss)
f.close()

print '\n'
for mss in arrays:
    print("Algorithm 1 (left,right,sum):" + str(maxSumSubarray.enumeration(mss)))
    print("Algorithm 2 (left,right,sum):" + str(maxSumSubarray.better_enumeration(mss)))
    print("Algorithm 3 (left,right,sum):" + str(maxSumSubarray.max_subarray_recursive(mss, 0, len(mss)-1)))
    print("Algorithm 4 (left,right,sum):" + str(maxSumSubarray.linear_time(mss)) + "\n")
