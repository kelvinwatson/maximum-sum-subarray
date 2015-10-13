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

#Algorithm 1:

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

#Algorithm 2:

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

#Algorithm 3: Divide and Conquer

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



#Algorithm 4:

def linear_time(array):
	# curr_best_sum = temp_sum = array[0]
	# left = right = 0
	# for i,v in enumerate(array[1:]):
	# 	temp_sum = max(array[1:][i], temp_sum+array[1:][i])
	# 	#NOTE: temp_sum is really temp_sum from left to i-1
	# 	if(temp_sum == array[1:][i]): left=i+1
	# 	curr_best_sum = max(curr_best_sum, temp_sum)
	# 	if(curr_best_sum == temp_sum): right=i+1
	# return (left,right,curr_best_sum)
    currBestSum = tempSum = tempLeft = left = 0
    right = -1
    for i,v in enumerate(array):
        if (tempSum + array[i]) < 0: #everything before is trumped
            tempLeft=i+1
            tempSum=0 #trash previous values and start counting from here!
        else:	#adding the array[i] to tempSum makes tempSum larger than before
            tempSum+=array[i]
        if tempSum > currBestSum:	#if tempSum results in a larger sum, then make it the best
            currBestSum = tempSum
            left = tempLeft
            right = i
    return (left,right,currBestSum)






#TEST SCRIPT
# vals1=[10,8,-255,-30,50,30050,8,50,-77,76,-75]
# vals2=[-2,1,8,2,-6,5,105]
# vals3=[1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
# vals4=[10,20,30,40,50]
# vals5=[-1,-1,-1,10000,-1,-1,-1]

# mss1=[1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
# mss2=[2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7, -2]
# mss3=[10, -11, -1, -9, 33, -45, 23, 24, -1, -7, -8, 19]
# mss4=[31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
# mss5=[3, 2, 1, 1, -8, 1, 1, 2, 3]
# mss6=[12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
# mss7=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

# print("--TESTING ALGORITHM 1---")
# #print(str(enumeration(vals1)))
# #print(str(enumeration(vals2)))
# #print(str(enumeration(vals3)))
# #print(str(enumeration(vals4)))
# #print(str(enumeration(vals5)))
#
# print(str(enumeration(mss1)))
# print(str(enumeration(mss2)))
# print(str(enumeration(mss3)))
# print(str(enumeration(mss4)))
# print(str(enumeration(mss5)))
# print(str(enumeration(mss6)))
# print(str(enumeration(mss7)))
# #
#
#
# print("---TESTING ALGORITHM 2---")
# #print(str(better_enumeration(vals1)))
# #print(str(better_enumeration(vals2)))
# #print(str(better_enumeration(vals3)))
# #print(str(better_enumeration(vals4)))
# #print(str(better_enumeration(vals5)))
# #
# print(str(better_enumeration(mss1)))
# print(str(better_enumeration(mss2)))
# print(str(better_enumeration(mss3)))
# print(str(better_enumeration(mss4)))
# print(str(better_enumeration(mss5)))
# print(str(better_enumeration(mss6)))
# print(str(better_enumeration(mss7)))
# #
# #
# print("---TESTING ALGORITHM 3---")
# # #print(str(max_subarray_recursive(vals1,0,10)))
# # #print(str(max_subarray_recursive(vals2,0,6)))
# # #print(str(max_subarray_recursive(vals3,0,9)))
# # #print(str(max_subarray_recursive(vals4,0,4)))
# # #print(str(max_subarray_recursive(vals5,0,6)))
#
# print(str(max_subarray_recursive(mss1,0,15)))
# print(str(max_subarray_recursive(mss2,0,14)))
# print(str(max_subarray_recursive(mss3,0,11)))
# print(str(max_subarray_recursive(mss4,0,9)))
# print(str(max_subarray_recursive(mss5,0,8)))
# print(str(max_subarray_recursive(mss6,0,9)))
# print(str(max_subarray_recursive(mss7,0,8)))
#
# print("---TESTING ALGORITHM 4---")
# # #print(str(linear_time(vals1)))
# # #print(str(linear_time(vals2)))
# # #print(str(linear_time(vals3)))
# # #print(str(linear_time(vals4)))
# # #print(str(linear_time(vals5)))
#
# print(str(linear_time(mss1)))
# print(str(linear_time(mss2)))
# print(str(linear_time(mss3)))
# print(str(linear_time(mss4)))
# print(str(linear_time(mss5)))
# print(str(linear_time(mss6)))
# print(str(linear_time(mss7)))