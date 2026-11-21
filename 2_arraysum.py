'''
Given an array arr of size n, the task is to find the sum of all the elements in the array.

Example 1:
Input: n=5, arr = [1,2,3,4,5]

Output: 15
'''
def array_sum(arr):
    total = 0

    for i in arr:
        total += i

    return total


n = 5
arr = [1, 2, 3, 4, 5]

print(array_sum(arr))

