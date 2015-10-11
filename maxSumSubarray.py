#!/usr/bin/env python
#title          :maxSumSubarray.py
#description    :finds the subarray with the maximum sum
#author         :project group 2: Joseph Barlan, Jeff Mueller, Kelvin Watson
#creation date  :9 October 2015
#last modified  :9 October 2015
#usage          :python maxSumSubarray.py
#notes          :
#python_version :2.6.6
#==============================================================================

#Algorithm 1:

def brute_force_enumeration(array):
    left = right = bestRight = currBestSum = tempSum = 0
    for i,v in enumerate(array):
        tempSum = loopSum = array[i]
        for j,v in enumerate(array[i+1:],i+1):
            tempSum = tempSum + array[j]
            if tempSum > loopSum:
                loopSum = tempSum
                right = j
        if loopSum>currBestSum:
            currBestSum = loopSum
            left = i
            bestRight = right
    return (left,bestRight,currBestSum)

#Algorithm 2:

def better_enumeration(array):
	currBestSum = tempSum = array[0]
	left = right = 0
	for i,v in enumerate(array[1:]):
		tempSum = max(array[1:][i], tempSum+array[1:][i])
		#NOTE: tempSum is really tempSum from left to i-1
		if(tempSum == array[1:][i]): left=i+1
		currBestSum = max(currBestSum, tempSum)
		if(currBestSum == tempSum): right=i+1
	return (left,right,currBestSum)

#Algorithm 3: Divide and Conquer

def max_cross_subarray(array, low, mid, high):
    """Returns the low index, high index, and sum of the subarray that crosses
    the middle of the array"""

    left_sum = right_sum = 0
    max_left=0
    max_right=0
    sum = 0
    #left_half = array[low:mid+1]
    #right_half = array[mid+1:high+1]

    for i, val in reversed(list(enumerate(array[low:mid+1]))):
        sum = sum + array[low:mid+1][i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    for j,val in enumerate(array[mid+1:high+1]):
        sum = sum + array[mid+1:high+1][j]
        if sum > right_sum:
            right_sum = sum
            max_right = j+mid+1

    return (max_left, max_right, left_sum + right_sum)


def max_subarray_recursive(array, low, high):
    """Returns the low index, high index, and sum of the subarray with max sum
    """

    if high == low:
        return (low, high, array[low])
    else:
        mid = (int)((low+high)/2)
        left_low, left_high, left_sum = max_subarray_recursive(array, low, mid)
        right_low, right_high, right_sum = max_subarray_recursive(array, mid+1, high)
        cross_low, cross_high, cross_sum = max_cross_subarray(array, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


#TEST SCRIPT

vals=[10,8,-255,-30,50,30050,8,50,-77,76,-75]
vals2=[-2,1,8,2,-6,5,105]
print("---TESTING ALGORITHM 1---")
print(str(brute_force_enumeration(vals)))
print(str(brute_force_enumeration(vals2)))
print("---TESTING ALGORITHM 2---")
print(str(better_enumeration(vals)))
print(str(better_enumeration(vals2)))
print("---TESTING ALGORITHM 3---")
print(str(max_subarray_recursive(vals,0,10)))
print(str(max_subarray_recursive(vals2,0,6)))

