# Question:
# Given an array nums of n integers, find the element that occurs
# the maximum number of times (highest frequency).
# If multiple elements have the same maximum frequency,
# return the smallest element among them.

def highest_occurring_element(nums):
    freq = {}

    # Count frequency of each element
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # Find the element with highest frequency.
    # In case of a tie, choose the smallest element.
    max_freq = 0
    result = float('inf')

    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            result = key

        elif value == max_freq:
            result = min(result, key)

    return result


nums = [1, 2, 2, 3, 3, 3, 2, 1]

print(highest_occurring_element(nums))



'''
inf
It is a special floating-point value that is greater than every 
finite numerical value.
Output:
Why do we use it in DSA?
Suppose you want to find the smallest number in an array.
You need an initial value that is greater than every possible array element.
'''
