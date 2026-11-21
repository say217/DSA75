'''. 

Given an array arr of size n, the task is to check if the 
given array is sorted in (ascending / Increasing / Non-decreasing) 
order. If the array is sorted then return True, else return False.

Example 1:
Input: n = 5, arr = [1,2,3,4,5]

Output: True

Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, 
So the answer is True '''

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


n = 5
arr = [1, 2, 3, 4, 5]

print(is_sorted(arr))




