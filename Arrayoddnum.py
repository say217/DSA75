'''
Given an array of n elements. The task is to return the count of the number of odd numbers in the array.

Example 1:
Input: n=5, array = [1,2,3,4,5]

Output: 3
'''
def count_odd(arr):
    count = 0

    for i in arr:
        if i % 2 != 0:
            count += 1

    return count


n = 5
arr = [1, 2, 3, 4, 5]

print(count_odd(arr))
