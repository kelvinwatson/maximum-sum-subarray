#!/usr/bin/env python
#title          :expStats.py
#description    :Script to capture runtime averages for max sum subarray
#                implementations
#author         :project group 2: Joseph Barlan, Jeff Mueller, Kelvin Watson
#creation date  :13 October 2015
#last modified  :13 October 2015
#usage          :python expStats.py
#notes          :
#python_version :2.6.6
#==============================================================================
import random
import maxSumSubarray
import time
import csv

#----------------------------------------------------------------
# UTILITY FUNCTIONS
#----------------------------------------------------------------

def random_array(n):
    """ returns a list of n integers with at least one positive integer"""
    has_pos_int = False
    while not has_pos_int:
        array = []
        for i in range(0, n):
            x = random.randint(-1000, 1000)
            if x > 0:
                has_pos_int = True
            array.append(x)
    return array

def create_ten_input_sizes(start, interval):
    """create array of 10 from start"""
    d = 30  #this is specified in the project, must have 10 different input sizes
    input_sizes = []
    for i in range(0, d):
        input_sizes.append(start + (i * interval))
    return input_sizes

def saveRunTime(algorithm, input_sizes, file_name):
    print "running"
    alg_time =[]
    #list to iterate specific to Alg 1
    for n in input_sizes:
        total_time = 0
        for i in range(0, 10):
            temp_array = random_array(n)
            start = time.clock()
            #call to algorithm function
            algorithm(temp_array)
            elapsed = time.clock() - start
            total_time += elapsed
        alg_time.append(total_time/10.0)


    #This opens the csv file and clears it, change
    #'wb' to 'ab' to append
    with open(file_name, 'ab') as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(input_sizes)
        statswriter.writerow(alg_time)
    print " >>>>> done! \n"


#----------------------------------------------------------------
# MAIN
#----------------------------------------------------------------

input_size = create_ten_input_sizes(100, 10, 'stats1.csv')
saveRunTime(maxSumSubarray.enumeration, input_size)

input_size = create_ten_input_sizes(100, 100)
saveRunTime(maxSumSubarray.better_enumeration, input_size, 'stats2.csv')
saveRunTime(maxSumSubarray.max_subarray_recursive, input_size, 'stats3.csv')
saveRunTime(maxSumSubarray.linear_time, input_size, 'stats4.csv')

