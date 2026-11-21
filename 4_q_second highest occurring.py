'''
Second Highest Occurring Element




Companies
Given an array of n integers, find the second most frequent element in it.

If there are multiple elements that appear second most frequent times, find the smallest of them.

If second most frequent element does not exist return -1.

Example 1:
Input: arr = [1, 2, 2, 3, 3, 3]

Output: 2

'''

def second_highest_occurrence(arr):

    freq = {}

    # Count frequency
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    first = 0
    second = 0

    # Find second highest frequency
    for count in freq.values():

        if count > first:
            second = first
            first = count

        elif count > second and count < first:
            second = count

    if second == 0:
        return -1

    ans = float('inf')

    # Find smallest element with second highest frequency
    for num in freq:
        if freq[num] == second:
            ans = min(ans, num)

    return ans


arr = [1, 2, 2, 3, 3, 3]
print(second_highest_occurrence(arr))


