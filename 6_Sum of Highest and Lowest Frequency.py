'''
Sum of Highest and Lowest Frequency

59


Companies
Given an array of n integers, find the sum of the frequencies of the highest occurring number and lowest occurring number.

Example 1:
Input: arr = [1, 2, 2, 3, 3, 3]

Output: 4

'''

def sum_highest_lowest(arr):

    freq = {}

    # Count frequency
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    highest = 0
    lowest = float('inf')

    # Find highest and lowest frequency
    for count in freq.values():

        if count > highest:
            highest = count

        if count < lowest:
            lowest = count

    return highest + lowest


arr = [1, 2, 2, 3, 3, 3]
print(sum_highest_lowest(arr))





