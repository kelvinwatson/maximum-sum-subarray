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

testCaseNum = 1
arrays = []
with open("MSS_TestProblems.txt", "r") as f:
    for line in f:
        line = line.replace("[", "")
        line = line.replace("]", "")
        line = line.replace("\n", "")
        mss = line.split(",")
        mss = [int(i) for i in mss]
        #print "Test Case ", testCaseNum, ":  ", mss
        arrays.append(mss)
        testCaseNum += 1
f.close()

print '\n'
testCaseNum = 1
with open("MSS_Results.txt", "w") as f:
    for mss in arrays:
        f.write("Test Case: " + str(testCaseNum) + "\n")
        f.write( str(mss) + "\n" )
        f.write("--------------------------------\n")
        f.write("Algorithm 1 (left,right,sum):" + str(maxSumSubarray.enumeration(mss)) + "\n")
        f.write("Algorithm 2 (left,right,sum):" + str(maxSumSubarray.better_enumeration(mss)) + "\n")
        f.write("Algorithm 3 (left,right,sum):" + str(maxSumSubarray.max_subarray_recursive(mss, 0, len(mss)-1)) + "\n")
        f.write("Algorithm 4 (left,right,sum):" + str(maxSumSubarray.linear_time(mss)) + "\n\n\n")
        testCaseNum += 1
f.close()
