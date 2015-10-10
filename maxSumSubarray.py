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


def max_cross_subarray(array, low, mid, high):
    """Returns the low index, high index, and sum of the subarray that crosses
    the middle of the array"""

    left_sum = right_sum = 0
    max_left = max_right = -1
    sum = 0
    print("array in max_cross_subarray function="+str(array))
    print("low="+str(low)+" mid="+str(mid)+" high="+str(high))
    left_half = array[low:mid+1]
    right_half = array[mid+1:high+1]
    print("left_half in max_cross_subarray function="+str(left_half))
    print("right_half in max_cross_subarray function="+str(right_half))

    for i, val in reversed(list(enumerate(array[low:mid+1]))):
        print("i="+str(i), "val="+str(val))
        sum = sum + array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    print("sum from left side="+str(sum))

    sum = 0
    for j,val in enumerate(array[mid+1:high+1]):
        print("j="+str(j), "val="+str(val))
        sum = sum + array[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def divide_and_conquer(array, low, high):
    """Returns the low index, high index, and sum of the subarray with max sum
    """

    if high == low:
        return (low, high, array[low])
    else:
        mid = (int)((low+high)/2)
        left_low, left_high, left_sum = divide_and_conquer(array, low, mid)
        right_low, right_high, right_sum = divide_and_conquer(array, mid+1, high)
        cross_low, cross_high, cross_sum = max_cross_subarray(array, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


#TEST SCRIPT
vals=[10,8,-255,-30,50,30050,8,50,-77,76,-75]
print(str(divide_and_conquer(vals,0,10)))

