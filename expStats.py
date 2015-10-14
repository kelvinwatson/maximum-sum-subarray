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

def runAlgorithm(alg, interval):
    """utility run a certain function n times"""
    rand_input = create_ten_input_sizes(100, interval)
    alg(rand_input)


#----------------------------------------------------------------
# Algorithm 1
#----------------------------------------------------------------
def algorithm1(alg_1_input_sizes):
    alg_time =[]
    #title specifice to Alg 1
    print "Enumeration - Algorithm 1"
    #list to iterate specific to Alg 1
    for n in alg_1_input_sizes:
        total_time = 0
        for i in range(0, 10):
            temp_array = random_array(n)
            start = time.clock()
            #call to algorithm function specific to Alg 1
            maxSumSubarray.enumeration(temp_array)
            elapsed = time.clock() - start
            total_time += elapsed
        alg_time.append(total_time/10.0)


    #This opens the csv file and clears it, change
    #'wb' to 'ab' to append
    with open('stats1.csv', 'ab') as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(alg_1_input_sizes)
        statswriter.writerow(alg_time)

    #input sizes specific to Alg 1
    #print alg_1_input_sizes
    #print alg_time


#----------------------------------------------------------------
# Algorithm 2
#----------------------------------------------------------------
def algorithm2(alg_2_input_sizes):
    alg_time =[]
    #title specifice to Alg
    print "Better Enumeration - Algorithm 2"
    #list to iterate specific to Alg
    for n in alg_2_input_sizes:
        total_time = 0
        for i in range(0, 10):
            temp_array = random_array(n)
            start = time.clock()
            #call to algorithm function specific to Alg
            maxSumSubarray.better_enumeration(temp_array)
            elapsed = time.clock() - start
            total_time += elapsed
        alg_time.append(total_time/10.0)


    with open('stats2.csv', 'ab') as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(alg_2_input_sizes)
        statswriter.writerow(alg_time)

    #input sizes specific to Alg
    #print alg_2_input_sizes
    



#----------------------------------------------------------------
# Algorithm 3
#----------------------------------------------------------------
def algorithm3(alg_3_input_sizes):
    alg_time =[]
    #title specifice to Alg
    print "Recursive - Algorithm 3"
    #list to iterate specific to Alg
    for n in alg_3_input_sizes:
        total_time = 0
        for i in range(0, 10):
            temp_array = random_array(n)
            start = time.clock()
            #call to algorithm function specific to Alg
            maxSumSubarray.max_subarray_recursive(temp_array, 0, len(temp_array) - 1)
            elapsed = time.clock() - start
            total_time += elapsed
        alg_time.append(total_time/10.0)

    with open('stats3.csv', 'ab') as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(alg_3_input_sizes)
        statswriter.writerow(alg_time)

    #input sizes specific to Alg
    #print alg_3_input_sizes
    #print alg_time



#----------------------------------------------------------------
# Algorithm 4
#----------------------------------------------------------------
def algorithm4(alg_4_input_sizes):
    alg_time =[]
    #title specifice to Alg
    print "Linear - Algorithm 4"
    #list to iterate specific to Alg
    for n in alg_4_input_sizes:
        total_time = 0
        for i in range(0, 10):
            temp_array = random_array(n)
            start = time.clock()
            #call to algorithm function specific to Alg
            maxSumSubarray.linear_time(temp_array)
            elapsed = time.clock() - start
            total_time += elapsed
        alg_time.append(total_time/10.0)

    with open('stats4.csv', 'ab') as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(alg_4_input_sizes)
        statswriter.writerow(alg_time)

    #input sizes specific to Alg
    #print alg_4_input_sizes
    #print alg_time


#----------------------------------------------------------------
# MAIN
#----------------------------------------------------------------

#runAlgorithm(algorithm1, 10)
#runAlgorithm(algorithm2, 100)
#runAlgorithm(algorithm3, 100)
runAlgorithm(algorithm4, 100)
    
