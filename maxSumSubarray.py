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


#Agorithm 3: Divide and Conquer

def max_cross_subarray(array, low, mid, high):
    """Returns the low index, high index, and sum of the subarray that crosses
    the middle of the array"""

    left_sum = right_sum = 0
    max_left=0
    max_right=0
    sum = 0
    print("array in max_cross_subarray function="+str(array))
    print("low="+str(low)+" mid="+str(mid)+" high="+str(high))
    left_half = array[low:mid+1]
    right_half = array[mid+1:high+1]
    print("left_half in max_cross_subarray function="+str(left_half))
    print("right_half in max_cross_subarray function="+str(right_half))

    for i, val in reversed(list(enumerate(array[low:mid+1]))):
        print("i="+str(i), "val="+str(val))
        sum = sum + array[low:mid+1][i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    print("left final: sum="+str(sum)+" left_sum="+str(left_sum))

    sum = 0
    for j,val in enumerate(array[mid+1:high+1]):
        print("j="+str(j), "val="+str(val))
        sum = sum + array[mid+1:high+1][j]
        print("sum after addition="+str(sum))
        if sum > right_sum:
            right_sum = sum
            print("right_sum="+str(right_sum))
            max_right = j+mid+1
    print("right final: sum="+str(sum)+" right_sum="+str(right_sum))

    print("left_sum+right_sum="+str(left_sum+right_sum))
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
print(str(max_subarray_recursive(vals,0,10)))

