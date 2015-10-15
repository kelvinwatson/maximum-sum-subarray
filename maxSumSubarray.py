#!/usr/bin/env python
#title          :maxSumSubarray.py
#description    :finds the subarray with the maximum sum
#author         :project group 2: Joseph Barlan, Jeff Mueller, Kelvin Watson
#creation date  :9 October 2015
#last modified  :11 October 2015
#usage          :python maxSumSubarray.py
#notes          :
#python_version :2.6.6
#==============================================================================


#-------------------------------------------------------------------------------
#Algorithm 1:
#-------------------------------------------------------------------------------
def enumeration(array):
    left = right = 0
    max_sum = array[0] #I added this line, else this kind of array fails [-2,-3,-4]
    for i,x in enumerate(array):
        for j,y in enumerate(array[i:],i):
            temp_sum=0
            for k,z in enumerate(array[i:j+1],i):
                temp_sum = temp_sum + z #accumulate sum for this pair
            if temp_sum > max_sum:
                max_sum = temp_sum
                left = i
                right = j
    return left,right,max_sum

#-------------------------------------------------------------------------------
#Algorithm 2:
#-------------------------------------------------------------------------------
def better_enumeration(array):
    left = right = best_right = curr_best_sum = temp_sum = 0
    for i,v in enumerate(array):
        temp_sum = loop_sum = array[i]
        for j,v in enumerate(array[i+1:],i+1):
            temp_sum = temp_sum + array[j]
            if temp_sum > loop_sum:
                loop_sum = temp_sum
                right = j
        if loop_sum>curr_best_sum:
            curr_best_sum = loop_sum
            left = i
            best_right = right
    return (left,best_right,curr_best_sum)

#-------------------------------------------------------------------------------
#Algorithm 3: Divide and Conquer
#-------------------------------------------------------------------------------
def max_cross_subarray(array, low, mid, high):
    """Returns the low index, high index, and sum of the subarray that crosses
    the middle of the array"""
    left_sum = float("-inf")
    max_left=0
    max_right=0
    sum = 0
    #for i, val in reversed(list(enumerate(array[low:mid+1],mid+1))):
    for i in reversed(range(low,mid+1)):
        sum = sum + array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum=float("-inf")
    sum = 0
    for j in range(mid+1,high+1):
        sum = sum + array[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def max_subarray_recursive(array, low, high):
    """Returns the low index, high index, and sum of the subarray with max sum"""
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


#-------------------------------------------------------------------------------
#Algorithm 4:
#-------------------------------------------------------------------------------
def linear_time(array):
    currBestSum = tempSum = tempLeft = left = 0
    right = -1
    for i,v in enumerate(array):
        if (tempSum + v) < 0:
            tempLeft=i+1
            tempSum=0
        else:	#adding the array[i] to tempSum makes tempSum larger than before
            tempSum+=v
        if tempSum > currBestSum:	#if tempSum results in a larger sum, then make it the best
            currBestSum = tempSum
            left = tempLeft
            right = i
    return (left,right,currBestSum)
